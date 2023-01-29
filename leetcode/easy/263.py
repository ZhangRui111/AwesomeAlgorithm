"""
tag: 数学
263. 丑数
https://leetcode.cn/problems/ugly-number/
"""
import math


class Solution0_0:
    """ 超时 """
    def isUgly(self, n: int) -> bool:
        n = abs(n)
        if n <= 6:
            return True

        for i in range(7, n + 1, 2):
            max_i = math.floor(math.sqrt(i))
            prime = True
            for j in range(3, max_i + 1, 2):
                if i % j == 0:
                    prime = False
                    break
            if prime and n % i == 0:
                return False
        return True


class Solution0_1:
    """ 错误，丑数被定义为正整数 """
    def isUgly(self, n: int) -> bool:
        n = abs(n)
        while n % 5 == 0:
            n //= 5
        while n % 3 == 0:
            n //= 3
        while n % 2 == 0:
            n //= 2
        if n == 1:
            return True
        else:
            return False


class Solution0_2:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 5 == 0:
            n //= 5
        while n % 3 == 0:
            n //= 3
        while n % 2 == 0:
            n //= 2
        if n == 1:
            return True
        else:
            return False


class Solution1:
    """ 官解 """
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor

        return n == 1

