"""Stack module."""


class Stack:

    def __init__(self):
        self._values = []

    def push(self, value):
        """Add element at stack"""
        self._values.append(value)

    def pop(self):
        """Remove and return last element from stack"""
        if self.is_empty:
            raise IndexError("Stack is empty")
        return self._values.pop()

    def peek(self):
        """Show had element of stack"""
        if self.is_empty:
            raise IndexError("Stack is empty")
        return self._values[-1]

    def is_empty(self):
        """Check of stack is empty"""
        return len(self._values) == 0

    def size(self):
        """Return stack size"""
        return len(self._values)
