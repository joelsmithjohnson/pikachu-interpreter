"""Provide the basic data structure and functions of the pikachu language.

Classes:
PikaStack -- The basic data structure of the pikachu language.
"""
class PikaStack():
    """Encapsulate Stack specific data and methods defined in the pikachu langeuage.

    PikaStack()
    ADD() -> void
    SUB() -> void
    MULT() -> void
    DIV() -> void
    POP() -> int, 'NaN', or None
    PUSH() -> void
    PEEK() -> int, 'NaN', or None
    EMPTY() -> bool
    """

    def __init__(self):
        """Construct a PikaStack object.
        """
        self.elements = []

    def ADD(self):
        """ Add the top two elements on the stack.

        Adds the top two elements on the stack and pushes the result back onto 
        the stack.
        
        Error handling:
        If the stack is empty, nothing happens.
        If the stack only has a single element, the result pushed to the top of
        the stack is float("NaN").
        """
        if self.__check_binary_op():
            a = self.POP()
            b = self.POP()
            self.PUSH(a+b)
    
    def SUB(self):
        """Subtracts the top two elements.
        
        Subtracts the first element on the stack from the second element and
        pushes the result back onto the stack.

        Error Handling:
        If the stack is empty, nothing happens.
        If the stack only has a single element, the result pushed to the top of
        the stack is float("NaN")
        """
        if self.__check_binary_op():
            a = self.POP()
            b = self.POP()
            self.PUSH(b-a)
    
    def MULT(self):
        """Multiplies the top two elements on the stack.

        Multiplies the top two elements on the stack and pushes the result back
        onto the stack.

        Error handling:
        If the stack is empty, nothing happens.
        If the stack only has a single element, the result pushed to the top of 
        the stack is float("NaN")
        """
        if self.__check_binary_op():
            a = self.POP()
            b = self.POP()
            self.PUSH(a*b)

    def DIV(self):
        """Divides the top two elements on the stack

        Divides the second element on the stack by the first element on the stack,
        and pushes the result back on top of the stack.
        
        Error Handling:
        If the stack is empty, nothing happens.
        If the stack only has a single element, the result pushed to the top of 
        the stack is float("NaN")
        If the divisor is '0', the result pushed to the top of the stack is 
        float("NaN")
        """
        if self.__check_binary_op():
            a = self.POP()
            b = self.POP()
            if a == 0:
                self.PUSH(float('NaN'))
            else:
                self.PUSH(b//a)

    def POP(self):
        """Pops and returns the top element from the stack.

        Error Handling:
        If the stack is empty None is returned.
        """
        if len(self.elements):
            return self.elements.pop()
        else:
            return None

    def PUSH(self, element):
        """Pushes an element to the top of the stack.

        Arguments:
        element -> The element to push on the top of the stack.
        """
        self.elements.append(element)

    def PEEK(self):
        """Returns the top element from the stack without removing it.

        Error Handling:
        If the stack is empty None is returned.
        """
        if len(self.elements):
            return self.elements[-1]
        else:
            return None

    def EMPTY(self):
        """Returns True if the stack is empty, false otherwise.
        """
        return len(self.elements) == 0


    def __check_binary_op(self):
        """Returns True if it is safe to perform a binary op, False otherwise.

        Verifies a binary operation can take place. If the stack is empty, 
        nothing happens. If the stack has a single element, it is replaced with
        float("NaN").

        Returns True if there are at least 2 elements on the stack.
        Returns False if there is 0 or 1 elements on the stack.
        """ 
        if not len(self.elements):
            return False
        if len(self.elements) == 1:
            self.elements[0] = float('NaN')
            return False
        return True
    
    def __str__(self):
        """Defines the string representation of the PikaStack object."""
        return str(self.elements)