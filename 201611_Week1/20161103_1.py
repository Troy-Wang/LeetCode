"""
Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.getMin() is None or x <= self.getMin():
            self.minStack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        value = self.stack.pop()
        if value == self.getMin():
            self.minStack.pop()
        return value

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.minStack:
            return None
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
