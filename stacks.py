"""LIFO stacks implemented with python list"""

class StackEmptyError(IndexError):
    """Operation cannot be completed on an empty stack."""

class Stack(object):
    """LIFO stack implemented via restriction on python list functionality.
    __Methods__: __init__, __repr__, __iter__
    User Methods: push, pop, peek, is_empty, empty, length
    Attributes: length
    """

    def __init__(self, inlist=None):
        """You can initialize this Stack with an existing list, otherwise
        initialization will be with an empty list."""
        if inlist:
            self._list = inlist
        else:
            self._list = []

    def push(self, item):
        """Push an item to the top of the stack"""

        self._list.append(item)

    def pop(self):
        """Pop an item off the top of the stack, return popped item"""

        if not self._list:
            raise StackEmptyError

        return self._list.pop()

    def peek(self):
        """Take a peek at the top of the stack"""

        return self._list[-1]

    def is_empty(self):
        """Checks if there are items on the stack, returns bool"""

        return not bool(self._list)

    def empty(self):
        """Empties the stack"""

        self._list = []

    def length(self):
        """Return length of stack."""

        return len(self._list)

    def __iter__(self):
        """Allows for iteration over the stack"""
        while True:
            try:
                yield self.pop()
            except StackEmptyError:
                raise StopIteration

    def __repr__(self):
        if not self._list:
            return "<Stack Empty>"
        else:
            return "<Stack head:{} length:{}".format(self._list[-1], 
                self.length)

def opposite_char(string):
    """takes on side of a paren and gives the other side
    sidedness matters"""
    if string == '{':
        return '}'
    elif string == '[':
        return ']'
    elif string == '(':
        return ')'

def is_balanced(string):
    """Checks to see if parentheses in a string are balanced properly.
    Handles (), [], and {}."""

    # Initialize the the stack 
    parens = Stack()
    for char in string:
        if char in ['(', '[', '{']:
            parens.push(char)
        elif char in [')', ']', '}']:
            if parens.is_empty():
            # There are no more to match with or the parens type doesn't match
                return False
            if char == opposite_char(parens.peek()):
                a = parens.pop()
                
    return parens.is_empty()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        for arg in sys.argv[1:]:
            if is_balanced(arg):
                print arg + 'is balanced.'
            else:
                print arg + 'is not balanced.'

























