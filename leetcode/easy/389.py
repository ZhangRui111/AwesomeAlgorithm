"""
tag: 字符串；哈希表；位运算；ASCII码
389. 找不同
https://leetcode.cn/problems/find-the-difference/
"""
from collections import Counter
from functools import reduce
from operator import xor


class Solution0_1:
    """ 计数 """
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t) - Counter(s))[0]


class Solution1_1:
    """ ASCII码求和 """
    def findTheDifference(self, s: str, t: str) -> str:
        # sum_s = sum_t = 0
        # for c in s:
        #     sum_s += ord(c)
        # for c in t:
        #     sum_t += ord(c)
        sum_t = sum(map(ord, t))
        sum_s = sum(map(ord, s))
        return chr(sum_t - sum_s)


class Solution1_2:
    """ 连接s和t后，只有 1 个数字出现了奇数次，其它数字全部出现偶数次，
    找出出现奇数次的数字 """
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(xor, map(ord, s + t)))
