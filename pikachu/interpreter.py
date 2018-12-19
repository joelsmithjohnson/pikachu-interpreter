"""Check the syntax and execute Pikachu commands.

Methods:
run -- The main context for the pikachu vm.
"""

import sys
from pikachu.utils import syntax_error
from pikachu.reader import PikaReader
from pikachu.stack import PikaStack

def run(fileName, args):
    """Run a specified Pikachu file in a virtual environment.

    Arguments:
    fileName -- the name and path of a file containing a pikachu program.
    args -- the command line arguments specified when the pikachu interpreter was
    run.
    """
    piStack = PikaStack()
    pikaStack = PikaStack()

    stackDict = {
        "pi pikachu": piStack,
        "pika pikachu": pikaStack
        }

    for a in args:
        piStack.PUSH(a)

    reader = PikaReader(fileName)
    while True:
        try:
            command = next(reader)
        except StopIteration:
            break
        terms = command.split()
        if len(terms) < 2:
            syntax_error(reader.lineNo)
        elif len(terms) < 3:
            command = " ".join(terms)
            if command == "pi pikachu":
                piStack.POP()
            elif command == "pika pikachu":
                pikaStack.POP()
            elif command == "pi pika":
                if not piStack.EMPTY():
                    pikaStack.PUSH(piStack.PEEK())
            elif command == "pika pi":
                if not pikaStack.EMPTY():
                    piStack.PUSH(pikaStack.PEEK())
            elif command == "pikachu pikachu":
                try:
                    lineNo = len(next(reader).split())
                except StopIteration:
                    syntax_error(reader.lineNo - 1)
                if piStack.PEEK() != pikaStack.PEEK():
                    continue
                reader.goto(lineNo)
            elif command == "pika pika":
                try:
                    lineNo = len(next(reader).split())
                except StopIteration:
                    syntax_error(reader.lineNo - 1)
                if piStack.PEEK() == pikaStack.PEEK():
                    continue
                reader.goto(lineNo)
            else:
                syntax_error(reader.lineNo)
        elif len(terms) < 4:
            try:
                tStack = stackDict[" ".join(terms[-2:])]
            except KeyError:
                syntax_error(reader.lineNo)
            command = terms[0]
            if command == "pikachu":
                tStack.DIV()
            else:
                tStack.PUSH(1)
        elif len(terms) < 5:
            try:
                tStack = stackDict[" ".join(terms[-2:])]
            except KeyError:
                syntax_error(reader.lineNo)
            command = " ".join(terms[:-2])
            if command == "pi pika":
                tStack.ADD()
            elif command == "pika pi":
                tStack.SUB()
            elif command == "pi pikachu":
                tStack.MULT()
            elif command == "pika pikachu":
                if not tStack.EMPTY():
                    print(tStack.POP(),end="")
                else:
                    print("undefined",end="")
            elif command == "pikachu pikachu":
                n = tStack.POP()
                if n != None and type(n) == int:
                    print(chr(n),end="")
                else:
                    print("undefined",end="")
            else:
                tStack.PUSH(2)
        else:
            try:
                tStack = stackDict[" ".join(terms[-2:])]
            except KeyError:
                syntax_error(reader.lineNo)
            tStack.PUSH(len(terms)-2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No Pika file specified")
        exit()
    fileName = sys.argv[1]
    try:
        args = [int(x) for x in sys.argv[2:]]
    except ValueError:
        print("invalid argument list: ",sys.argv[2:])
        exit()
    run(fileName, args)
