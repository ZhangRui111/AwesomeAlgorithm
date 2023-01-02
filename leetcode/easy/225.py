"""
tag: 栈；设计；队列
225. 用队列实现栈
https://leetcode.cn/problems/implement-stack-using-queues/
"""
from collections import deque


class MyStack1:

    def __init__(self):
        self.stacks = [deque(), deque()]
        self.flag = 0

    def push(self, x: int) -> None:
        self.stacks[self.flag].append(x)

    def pop(self) -> int:
        len_src = len(self.stacks[self.flag])
        for i in range(len_src - 1):
            a = self.stacks[self.flag].popleft()
            self.stacks[1 - self.flag].append(a)
        pop_item = self.stacks[self.flag].popleft()
        self.flag = 1 - self.flag
        return pop_item

    def top(self) -> int:
        return self.stacks[self.flag][-1]

    def empty(self) -> bool:
        return not self.stacks[self.flag]


class MyStack2:
    """ Use 2 queues """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queueA = deque()
        self.queueB = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queueB.append(x)
        while self.queueA:
            self.queueB.append(self.queueA.popleft())
        self.queueA, self.queueB = self.queueB, self.queueA

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queueA.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queueA[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queueA


class MyStack3:
    """ Use 1 queue """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.len_queue = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for _ in range(self.len_queue):
            self.queue.append(self.queue.popleft())
        self.len_queue += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue
