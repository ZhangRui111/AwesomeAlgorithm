"""
tag: 数学；动态规划；递归
剑指 Offer 10- I. 斐波那契数列
https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/
"""


class Solution0:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a + b
        return b % 1000000007


class Solution1:
    """ 中间结果取余 """
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, (a + b) % 1000000007
        return b


class Solution2:
    """ 矩阵快速幂解法 O(logN) """
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) \
                              % 1000000007
            return c

        def matrix_pow(a: List[List[int]], n: int) -> List[List[int]]:
            ret = [[1, 0], [0, 1]]
            while n > 0:
                if n & 1:
                    ret = multiply(ret, a)
                n >>= 1
                a = multiply(a, a)
            return ret

        res = matrix_pow([[1, 1], [1, 0]], n - 1)
        return res[0][0]


# **前置知识**
#
# 快速幂算法原理:
#
#   如需求数据 a 的幂次，此处 a 可以为数也可以为矩阵，常规做法需要对a进行不断的乘积即：
#   a * a * a * ... 此处的时间复杂度将为 O(n)
#
# 以求 3^10 的结果为例：
#
# [优化步骤1：]
#
# 易知：
#
# 3^10=3*3*3*3*3*3*3*3*3*3
#
#     =9^5 = 9^4*9
#
#     =81^2*9
#
#     =6561*9
#
# 基于以上原理，我们在计算一个数的多次幂时，可以先判断其幂次的奇偶性，然后：
#
#   如果幂次为偶直接 base(底数) 作平方，power(幂次) 除以2
#
#   如果幂次为奇则底数平方，幂次整除于2然后再多乘一次底数
#
# [优化步骤2：]
#
# 对于以上涉及到 [判断奇偶性] 和 [除以2] 这样的操作。使用系统的位运算比普通运算的效率
# 是高的，因此可以进一步优化：
#
#   把 power % 2 == 1 变为 (power & 1) == 1
#
#   把 power = power / 2 变为 power = power >> 1
