"""
tag:
剑指 Offer 16. 数值的整数次方
https://drive.mindmup.com/map/1Ai_K_IePWfAhWmpo-k1ftur4QqHtzmR3
"""


class Solution0:
    """ 快速幂算法 (迭代版本) """
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n > 0:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


class Solution1:
    """ 快速幂算法 (递归版本) """
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
