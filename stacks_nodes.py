"""LIFO stacks implemented with Nodes"""

class Node(object):
    """Nodes for linked list in stack"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return '<data:{}, next:{}>'.format(self.data, self.next)

class StackEmptyError(IndexError):
    """Operation cannot be completed on an empty stack."""

class Stack(object):
    """Implementing a stack with a linked list"""

    def __init__(self, item=None):
        """Initialize with head and tail pointing to None or the given node"""
        if item:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.head = None
            self.tail = None

    def push(self, item):
        """Create the next node"""
        # For stacks where a tail node exists
        if self.tail:
            previous = self.tail
            self.tail.next = Node(item)
            self.tail = self.tail.next
            self.tail.previous = previous
        # For pushing an initial node
        else:
            self.head = Node(item)
            self.tail = self.head

    def pop(self):
        """Remove the top item from the stack"""
        if not self.head:
            raise StackEmptyError
        elif self.head == self.tail:
            self.tail = None
            self.head = None
        else:
            self.tail.previous.next = None
            self.tail = self.tail.previous

    def peek(self):
        """Show what's at the top of the stack"""
        return self.tail.data

    def is_empty(self):
        return bool(self.head)


    def __repr__(self):
        if self.head:
            return '<head:{}, tail:{}, tail.prev.data:{}>'.format(self.head.data, self.tail.data, self.tail.previous.data)
        else:
            return '<None>'

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
