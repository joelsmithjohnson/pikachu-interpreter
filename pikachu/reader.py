"""Provide a basic assembler for the pikachu language.

Classes:
PikaReader -- The basic pikachu assembler
"""
from pikachu.utils import syntax_error

class PikaReader():
    """Provide a basic pikachu assembler and command parser.
    
    Methods:
    PikaReader(fileName) -> PikaReader
    goto(lineNo) -> void
    """
    def __init__(self, fileName):
        """Construct a PikaReader Object.

        Arguments:
        fileName -> the path to a pika file.
        """
        try:
            fi = open(fileName)
        except FileNotFoundError:
            print("No file named: {}".format(fileName))
            exit()
        l = fi.readlines()
        self.lines = {x:l[x].strip() for x in range(len(l))}
        self.lineNo = -1
        fi.close()


    def __next__(self):
        """Provide support for the next() function.

        next(this) is used to iterate through the pikachu code a line at a time.
        
        Exceptions:
        StopIteration -- when the end of the file has been reached.
        """
        self.lineNo += 1
        if self.lineNo >= len(self.lines):
            raise StopIteration
        line = self.lines[self.lineNo]
        line = line.split("//")[0]
        if not line:
            return self.__next__()
        
        #check for invalid repetition of pi, pika, pikachu
        target = None
        reps = 0
        for term in line.split():
            if term == target:
                reps += 1
                if reps >= 3:
                    syntax_error(self.lineNo)
            else:
                target = term
                reps = 1

        return line

    def goto(self, lineNo):
        """Directs the reader to a specific line of code.

        Arguments:
        lineNo -- the line of code (1 based) to set the reader to.
        
        Error Handling:
        If lineNo is greater than the number of lines in the code. The reader 
        will be set at the end of the code.
        """
        if lineNo >= len(self.lines):
            lineNo = len(self.lines)
        self.lineNo = lineNo - 2
