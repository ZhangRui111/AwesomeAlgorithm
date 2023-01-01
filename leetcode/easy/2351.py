"""
tag: 哈希表；字符串；计数
2351. 第一个出现两次的字母
https://leetcode.cn/problems/first-letter-to-appear-twice/
"""


class Solution0:
    """ 哈希表 """
    def repeatedCharacter(self, s: str) -> str:
        ht = [0] * 26
        for c in s:
            n = ord(c) - 97
            if ht[n]:
                return c
            else:
                ht[n] = 1


class Solution1:
    """ 哈希表 (set) """
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)


class Solution2:
    """ 位运算
    可以认为是 Solution0 的状态压缩优化 """
    def repeatedCharacter(self, s: str) -> str:
        seen = 0
        for ch in s:
            x = ord(ch) - ord("a")
            if seen & (1 << x):
                return ch
            seen |= (1 << x)
