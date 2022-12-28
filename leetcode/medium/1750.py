"""
tag: 双指针；字符串
1750. 删除字符串两端相同字符后的最短长度
https://leetcode.cn/problems/minimum-length-of-string-after-deleting-similar-ends/
"""
from itertools import groupby


class Solution0:
    """ groupby() """
    def minimumLength(self, s: str) -> int:
        res = len(s)
        ls = [(k, len(list(g))) for k, g in groupby(s)]
        n_ls = len(ls)
        left, right = 0, n_ls - 1
        while left <= right:
            if left == right:  # special case that must be considered
                if ls[left][1] > 1:
                    return 0
                else:
                    return 1

            if ls[left][0] == ls[right][0]:
                res -= (ls[left][1] + ls[right][1])
                left += 1
                right -= 1
            else:
                break
        return res


class Solution1:
    """ 官解 """
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            c = s[left]
            while left <= right and s[left] == c:  # "="很重要，"aabccccbba"
                left += 1
            while right >= left and s[right] == c:
                right -= 1
        return right - left + 1
