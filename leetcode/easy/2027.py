"""
tag: 字符串；贪心
2027. 转换字符串的最少操作次数
https://leetcode.cn/problems/minimum-moves-to-convert-string/
"""


class Solution1:
    """ 模拟 """
    def minimumMoves(self, s: str) -> int:
        covered = -1
        cnt = 0
        for i, c in enumerate(s):
            if c == 'X' and i > covered:
                cnt += 1
                covered = i + 2
        return cnt


class Solution2:
    """ 贪心：
    遍历字符串 s，只要遇到 'X'，指针 i 就直接往后移动三格，并且答案加 1；
    否则指针 i 往后移动一格。"""
    def minimumMoves(self, s: str) -> int:
        cnt = 0
        i = 0
        ns = len(s)
        while i < ns:
            if s[i] == 'X':
                cnt += 1
                i += 3
            else:
                i += 1
        return cnt
