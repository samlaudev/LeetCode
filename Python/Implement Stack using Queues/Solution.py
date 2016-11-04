# Problem: Implement Stack using Queues
#
# Implement the following operations of a stack using queues.
#
#   1. push(x) -- Push element x onto stack.
#   2. pop() -- Removes the element on top of the stack.
#   3. top() -- Get the top element.
#   4. empty() -- Return whether the stack is empty.
#
# Notes:
#
#   1. You must use only standard operations of a queue -- which means only push to back,
#       peek/pop from front, size, and is empty operations are valid.
#   2. Depending on your language, queue may not be supported natively.
#       You may simulate a queue by using a list or deque (double-ended queue),
#       as long as you use only standard operations of a queue.
#   3. You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
#
################################################################################

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.list.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.list.pop()


    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.list[len(self.list) - 1]
        else:
            return None


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.list) == 0
