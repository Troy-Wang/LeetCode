"""
Implement Stack using Queues
"""


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue = [x] + self.queue

    def pop(self):
        """
        :rtype: nothing
        """
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[0]
        else:
            return None

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue
