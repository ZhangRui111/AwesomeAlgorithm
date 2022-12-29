"""
tag: 字符串
剑指 Offer 05. 替换空格
https://leetcode.cn/problems/ti-huan-kong-ge-lcof/?favorite=xb9nqhhg
"""


class Solution0:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')


class Solution1:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == " ":
                res.append("%20")
            else:
                res.append(c)
        return "".join(res)
