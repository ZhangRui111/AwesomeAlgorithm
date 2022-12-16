"""
tag: 字符串
1945. 字符串转化后的各位数字之和
https://leetcode.cn/problems/sum-of-digits-of-string-after-convert/
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = "".join(str(ord(c) - ord('a') + 1) for c in s)
        for _ in range(k):
            s = str(self.transform(s))
        return int(s)

    def transform(self, s: str):
        return sum(int(c) for c in s)

