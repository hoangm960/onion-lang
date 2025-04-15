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
    tokens = re.findall(r'\(|\)|[^\s()]+', tree_str)

    return parse_helper(tokens)
