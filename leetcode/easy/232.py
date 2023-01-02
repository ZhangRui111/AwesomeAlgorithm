"""
tag: 栈；设计；队列
232. 用栈实现队列
https://leetcode.cn/problems/implement-queue-using-stacks/
"""


class MyQueue1:
    """ My solution """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackA = []
        self.stackB = []

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


class MyQueue2:
    """ 更高效：一个栈只负责入队，一个栈只负责出队 """
    def __init__(self):
        self.stack_in, self.stack_out = [], []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if self.stack_out:
            return self.stack_out[-1]
        else:
            return self.stack_in[0]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
