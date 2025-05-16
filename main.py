#!/usr/bin/env python3
"""
Onion Language - Main Entry Point

This script provides access to all Onion tools:
- REPL (for interactive expression evaluation)
- File Runner (for executing Onion programs)
"""

import sys
import argparse
from src import repl
from src import onion_runner

def main():
    # Define command line arguments
    parser = argparse.ArgumentParser(
        prog='Onion',
        description="Onion Programming Language Tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Start the REPL for interactive evaluation
  Onion repl

  # Run one or more Onion files
  Onion run file1.onion file2.onion
  
  # Default behavior (no arguments) starts the REPL
"""
    )
    
    # Define subcommands
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # REPL command
    repl_parser = subparsers.add_parser("repl", help="Start the interactive REPL")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run one or more Onion files")
    run_parser.add_argument("files", nargs="+", help="One or more Onion files to execute")
    run_parser.add_argument("-v", "--verbose", action="store_true", help="Print additional information during execution")
    run_parser.add_argument("--ast", action="store_true", help="Save AST for each file (saved to tests/output/)")
    run_parser.add_argument("--debug", action="store_true", help="Enable debug logging with detailed error information")
    
    # Parse arguments
    args = parser.parse_args()
    
    # If no command is specified, default to REPL
    if not args.command:
        repl.main()
        return 0
    
    # Execute the specified command
    if args.command == "repl":
        repl.main()
        return 0
    elif args.command == "run":
        # Forward arguments to onion_runner's main function
        sys.argv = [sys.argv[0]] + args.files
        if args.verbose:
            sys.argv.append("-v")
        if args.ast:
            sys.argv.append("--ast")
        if args.debug:
            sys.argv.append("--debug")
        return onion_runner.main()
    
    # This should not be reached
    return 1

if __name__ == "__main__":
    sys.exit(main())