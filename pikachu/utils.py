"""Provide common functions to the other modules in pikachu

Methods:
syntax_error -- print information about syntax errors in the pikachu program
"""

def syntax_error(lineNo):
    """Display information about syntax errors in the pikachu program then exit.

    Arguments:
    lineNo -- the line where the syntax error was found.
    """
    print("\nSyntax Error on line: {}".format(lineNo))
    exit()