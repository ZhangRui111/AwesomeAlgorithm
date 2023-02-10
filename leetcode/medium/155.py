"""
tag: 栈，设计
155. 最小栈
https://leetcode.cn/problems/min-stack/
"""

# 同 剑指 Offer 30. 包含min函数的栈 (easy)

import math


class MinStack1:
    """ 用辅助栈存储最小值 """
    def __init__(self):
        self.stack = []
        self.min_val = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_val.append(min(val, self.min_val[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]


class MinStack2(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-1)
# print(minStack.getMin())
# print(minStack.top())
# minStack.pop()
# print(minStack.getMin())
