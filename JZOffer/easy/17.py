"""
tag: 数组；数学
剑指 Offer 17. 打印从1到最大的n位数
https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/?favorite=xb9nqhhg
"""


class Solution0:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10 ** n))


# 剑指Offer上是要求打印大数的，建议直接抛开提交代码的限制，假定题目的要求为返回
# vector<string>

class Solution1:
    """ self.nine 和 self.start 是为了删除高位多余的 0 """
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            if x == n:
                s = "".join(num[self.start:])
                if s != '0':
                    res.append(s)
                if n - self.start == self.nine:
                    self.start -= 1
            else:
                for i in range(10):
                    if i == 9:
                        self.nine += 1
                    num[x] = str(i)
                    dfs(x + 1)
                self.nine -= 1

        self.nine = 0
        self.start = n - 1
        num, res = ['0'] * n, []
        dfs(0)
        return ",".join(res)
