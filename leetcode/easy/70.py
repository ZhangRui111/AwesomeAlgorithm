"""
tag: 动态规划
70. 爬楼梯
https://leetcode.cn/problems/climbing-stairs/
"""

# 同 剑指 Offer 10- II. 青蛙跳台阶问题 (easy)


class Solution0:
    """ Recursion (time-consuming) """
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution1:
    """ DP """
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]


class Solution2:
    """ DP (优化空间版) """
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b
