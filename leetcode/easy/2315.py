"""
tag: 字符串
2315. 统计星号
https://leetcode.cn/problems/count-asterisks/
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt = 0
        flag = True
        for c in s:
            if c == '|':
                flag = not flag
            if c == '*' and flag:
                cnt += 1
        return cnt
