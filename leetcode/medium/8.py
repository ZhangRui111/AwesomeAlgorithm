"""
tag: 字符串
8. 字符串转换整数 (atoi)
https://leetcode.cn/problems/string-to-integer-atoi/
"""


class Solution0:
    def myAtoi(self, s: str) -> int:
        POS_MAX = 2 ** 31 - 1
        NEG_MAX = -2 ** 31

        s = s.strip()

        if not s:  # ''
            return 0

        pos_flag = True
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            pos_flag = False

        nums = []
        for char in s:
            if '0' <= char <= '9':
                nums.append(int(char))
            else:
                break

        if not nums:  # []
            return 0

        res = 0
        for n in nums:
            res = res * 10 + n

        if pos_flag:
            return min(res, POS_MAX)
        else:
            return max(-res, NEG_MAX)
