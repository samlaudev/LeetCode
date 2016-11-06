# Problem: Implement Queue using Stacks
#
# Implement the following operations of a queue using stacks.
#
#   1. push(x) -- Push element x to the back of queue.
#   2. pop() -- Removes the element from in front of queue.
#   3. peek() -- Get the front element.
#   4. empty() -- Return whether the queue is empty.
#
# Notes:
#   1. You must use only standard operations of a stack -- which means only push to top,
#       peek/pop from top, size, and is empty operations are valid.
#   2. Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue),
#       as long as you use only standard operations of a stack.
#   3. You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
#
################################################################################

class Queue(object):
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
        return self.list.pop(0)


    def peek(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.list[0]
        else:
            return None


    def empty(self):
        """
        :rtype: bool
        """
        return not len(self.list) 
