"""
tag:
232. 用栈实现队列
https://leetcode.cn/problems/implement-queue-using-stacks/
"""


from collections import deque


class MyQueue1:
    """ My solution """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackA = deque()
        self.stackB = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        self.stackA.append(x)
        while self.stackB:
            self.stackA.append(self.stackB.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stackA.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stackA[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stackA
