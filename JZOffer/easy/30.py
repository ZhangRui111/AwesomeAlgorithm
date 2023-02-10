"""
tag: 栈；设计
剑指 Offer 30. 包含min函数的栈
https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/?favorite=xb9nqhhg
"""
from collections import deque


class MinStack0:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = deque()

    def push(self, x: int) -> None:
        if self.q:
            self.q.append((x, min(self.min(), x)))
        else:
            self.q.append((x, x))

    def pop(self) -> None:
        if self.q:
            self.q.pop()

    def top(self) -> int:
        return self.q[-1][0]

    def min(self) -> int:
        return self.q[-1][1]


class MinStack:
    """ 用辅助栈存储最小值 """
    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]
