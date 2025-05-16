#!/usr/bin/env python3
"""
Onion Runner - Execute Onion program files

This script allows running one or more Onion files in sequence.
Usage: python onion_runner.py [files...]
"""

import os
import sys
import argparse
import traceback
import logging
from src.interpreter import Interpreter
from src.parser import Parser

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger('onion_runner')

def run_onion_file(filename, interpreter, verbose=False, debug=False):
    """
    Execute an Onion file using the provided interpreter.
    
    Args:
        filename: Path to the Onion file
        interpreter: The Onion interpreter instance
        verbose: Whether to print additional information during execution
        debug: Whether to print detailed debug information
    
    Returns:
        A tuple (success, result) where:
        - success: Boolean indicating if execution completed without errors
        - result: The result of the program execution (which may be None even for successful runs)
    """
    try:
        # Ensure file exists
        if not os.path.exists(filename):
            logger.error(f"File '{filename}' not found")
            return False, None
            
        # Read file contents
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if verbose:
            logger.info(f"Running file: {filename}")
            
        # Parse the file
        parser = Parser()
        try:
            tree = parser.parse_input(content)
            
            if not tree:
                error = parser.get_last_error()
                if error:
                    logger.error(f"Failed to parse '{filename}': {error}")
                else:
                    logger.error(f"Failed to parse '{filename}': Unknown parsing error")
                
                if debug:
                    logger.debug("Parser error details:")
                    if hasattr(error, 'original_exception') and error.original_exception:
                        logger.debug(f"Original exception: {type(error.original_exception).__name__}")
                    logger.debug(f"File content:\n{content}")
                return False, None
                
        except Exception as e:
            logger.error(f"Failed to parse '{filename}': {str(e)}")
            if debug:
                logger.debug("Parser error details:")
                logger.debug(traceback.format_exc())
                logger.debug(f"File content:\n{content}")
            return False, None
            
        # Execute the program
        try:
            result = interpreter.visit(tree)
            
            # In verbose mode, report the final result
            if verbose and result is not None:
                logger.info(f"Result: {result}")
                
            return True, result
        except Exception as e:
            logger.error(f"Error executing '{filename}': {str(e)}")
            if debug:
                logger.debug("Execution error details:")
                logger.debug(traceback.format_exc())
                
                # Show the line of code where the error occurred if possible
                if hasattr(e, 'line') and hasattr(e, 'column'):
                    lines = content.split('\n')
                    if 0 <= e.line - 1 < len(lines):
                        error_line = lines[e.line - 1]
                        pointer = ' ' * (e.column - 1) + '^'
                        logger.debug(f"\nLine {e.line}:\n{error_line}\n{pointer}")
            return False, None
            
    except Exception as e:
        logger.error(f"Error processing '{filename}': {str(e)}")
        if debug:
            logger.debug("Processing error details:")
            logger.debug(traceback.format_exc())
        return False, None

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Execute Onion program files")
    parser.add_argument("files", nargs="+", help="One or more Onion files to execute")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print additional information during execution")
    parser.add_argument("--ast", action="store_true", help="Save AST for each file (saved to tests/output/)")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging with detailed error information")
    
    args = parser.parse_args()
    
    # Set logging level based on debug flag
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled")
    
    # Create a single interpreter instance for all files
    # Use non-REPL mode since we're running files, not interactive commands
    interpreter = Interpreter(is_repl_mode=False)
    
    # Process each file in sequence
    results = {}
    has_errors = False
    
    for filename in args.files:
        # Add .onion extension if missing
        if not filename.endswith('.onion'):
            full_filename = filename + '.onion'
        else:
            full_filename = filename
            
        # Support relative paths from tests/input directory
        if not os.path.isabs(full_filename) and not os.path.exists(full_filename):
            test_path = os.path.join('tests', 'input', full_filename)
            if os.path.exists(test_path):
                full_filename = test_path
                if args.verbose:
                    logger.info(f"Using test file: {test_path}")
            else:
                logger.error(f"File not found: {filename}")
                has_errors = True
                continue
        
        # Run the file
        success, result = run_onion_file(full_filename, interpreter, 
                                         verbose=args.verbose, debug=args.debug)
        results[full_filename] = result
        
        # Track if any file had errors
        if not success:
            has_errors = True
        
        # Generate AST if requested
        if args.ast and os.path.exists(full_filename):
            try:
                # Create output directory
                output_dir = os.path.join('tests', 'output')
                os.makedirs(output_dir, exist_ok=True)
                
                # Parse file again to get clean AST
                with open(full_filename, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                parser = Parser()
                tree = parser.parse_input(content)
                
                if tree:
                    # Save AST to file
                    base_name = os.path.basename(full_filename)
                    ast_file = os.path.join(output_dir, f"{os.path.splitext(base_name)[0]}.ast")
                    
                    with open(ast_file, 'w', encoding='utf-8') as f:
                        f.write(f"# AST for {base_name}\n\n")
                        f.write(parser.get_str_tree())
                    
                    if args.verbose:
                        logger.info(f"AST saved to: {ast_file}")
                else:
                    logger.error(f"Failed to generate AST for '{full_filename}': No parse tree generated")
                    has_errors = True
            except Exception as e:
                logger.error(f"Error generating AST for '{full_filename}': {str(e)}")
                if args.debug:
                    logger.debug(traceback.format_exc())
                has_errors = True
    
    # In verbose mode, summarize all results
    if args.verbose and len(args.files) > 1:
        logger.info("\nExecution Summary:")
        logger.info("-----------------")
        for filename, result in results.items():
            success = filename in results and not has_errors
            status = "Success" if success else "Failed"
            logger.info(f"{os.path.basename(filename)}: {status}")
    
    # Return failure exit code only if we encountered actual errors
    return 1 if has_errors else 0

if __name__ == "__main__":
    sys.exit(main()) 