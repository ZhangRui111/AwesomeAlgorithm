"""
tag: 数学；动态规划；递归
剑指 Offer 10- II. 青蛙跳台阶问题
https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
"""


class Solution0:
    """ 从 n=3 开始用转移方程求解 """
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(n - 2):
            a, b = b, (a + b) % 1000000007
        return b


class Solution1:
    """ 从 n=2 开始用转移方程求解 """
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        a, b = 1, 1
        for i in range(n - 1):
            a, b = b, (a + b) % 1000000007
        return b
