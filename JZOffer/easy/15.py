"""
tag: 位运算
剑指 Offer 15. 二进制中1的个数
https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/?favorite=xb9nqhhg
"""


class Solution0:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')


class Solution1_1:
    """ 循环检查二进制位 + 位与运算；
    时间复杂度：O(k)，其中 k 是 int 型的二进制位数，k=32"""
    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret


class Solution1_2:
    """ 位运算优化:
    n & (n - 1) 这一运算把 n 的二进制位中的最低位的 1 变为 0 """
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:  # 不断计算 n & (n - 1)，直到 n 变为 0 即可
            n &= n - 1
            ret += 1
        return ret
