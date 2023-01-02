"""
tag: 栈；设计；队列
剑指 Offer 09. 用两个栈实现队列
https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/?favorite=xb9nqhhg
"""


class CQueue1:
    """ Same as the 题库 232题 """
    def __init__(self):
        self.stackA, self.stackB = [], []

    def appendTail(self, value: int) -> None:
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        self.stackA.append(value)
        while self.stackB:
            self.stackA.append(self.stackB.pop())

    def deleteHead(self) -> int:
        if self.stackA:
            return self.stackA.pop()
        else:
            return -1


class CQueue2:
    """ 一个栈只负责入队，一个栈只负责出队 """
    def __init__(self):
        self.stack_in, self.stack_out = [], []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop() if self.stack_out else -1
