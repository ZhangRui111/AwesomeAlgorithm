"""
tag: 数学；动态规划
剑指 Offer 14- I. 剪绳子
https://leetcode.cn/problems/jian-sheng-zi-lcof/
"""


class Solution0:
    """ 数学 + 幂次乘法优化
    (1) 当所有绳段长度相等时，乘积最大。(2) 最优的绳段长度为 33
    切割：分出皆可能多的 3，如果余数为 1，就把最后一个 3 + 1 分割为 2 + 2 """
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        def quick_power(base, power):
            # 快速幂次乘法优化
            res = 1
            while power > 0:
                if power & 1:
                    res *= base
                base *= base
                power >>= 1
            return res

        a, b = n % 3, n // 3
        if a == 0:
            return quick_power(3, b)
        elif a == 1:
            return quick_power(3, b - 1) * 4
        else:
            return quick_power(3, b) * 2


class Solution1:
    """ 动态规划 """
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
