import re


def parse_helper(tokens, depth=0):
    output = ""
    while tokens:
        token = tokens.pop(0)

        if token == '(':
            # Check for empty node and skip if found
            if tokens and tokens[0] == ')':
                tokens.pop(0)
                continue
                
            # If next token is another opening parenthesis, process it recursively
            # without adding a new node line
            if tokens and tokens[0] == '(':
                output += parse_helper(tokens, depth)
                continue
                
            node = tokens.pop(0)
            output += " " * depth + f"{node}:\n"
            output += parse_helper(tokens, depth + 1)
        elif token == ')':
            return output
        else:
            output += " " * depth + \
                f"{token}{'' if tokens and tokens[0] == ')' else ':'}\n"
    return output


def beautify_parse_tree(tree_str):
    """
    Convert a lisp-style parse tree string to a more readable indented format.
    Removes extra parentheses and properly indents nested structures.
    """
    # Clean up the tree string first to handle any special cases
    tree_str = tree_str.replace('(:', '( :')  # Add space between ( and : for better parsing
    
    # Tokenize the tree string
    tokens = re.findall(r'\(|\)|[^\s()]+', tree_str)
    
    # Process the tokens into a formatted tree
    return parse_helper(tokens)
