"""Provide package level functionality for the pikachu interpreter.

Command line interface:

$ python -m pikachu filename [args]

"""
import sys
from pikachu.interpreter import run

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