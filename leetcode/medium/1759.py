"""
tag: 字符串；数学
1759. 统计同构子字符串的数目
https://leetcode.cn/problems/count-number-of-homogenous-substrings/
"""
from collections import defaultdict
from itertools import groupby


class Solution1:
    """
    思路：
    长度为 m 的完全相同字符串的同构子字符串的数目为 1 + 2 + ... + m
    1. 统计所有完全相同字符串的长度
    2. 使用 tmp 避免重复计数
    """
    def countHomogenous(self, s: str) -> int:
        cnt = defaultdict(int)
        sub = s[0]
        for c in s[1:]:
            if c == sub[-1]:
                sub += c
            else:
                cnt[len(sub)] += 1
                sub = c
        cnt[len(sub)] += 1

        res = 0
        tmp = 0
        max_val = max(cnt.keys())
        for i in range(1, max_val + 1):
            tmp += i  # 此时tmp的值: 长度为i的完全相同字符串的同构子字符串数目
            res += tmp * cnt[i]
        return res % (10 ** 9 + 7)


class Solution:
    """ 官解 """
    def countHomogenous(self, s: str) -> int:
        res = 0
        for k, g in groupby(s):
            n = len(list(g))
            res += (n + 1) * n // 2
        return res % (10 ** 9 + 7)
