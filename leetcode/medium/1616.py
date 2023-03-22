"""
tag: 双指针；字符串
1616. 分割两个字符串得到回文串
https://leetcode.cn/problems/split-two-strings-to-make-palindrome/
"""


class Solution0:

    def check(self, s):
        """ 回文串判断 """
        return s == s[::-1]

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)

        pre_a, suf_b = 0, n - 1
        while pre_a < suf_b:
            if a[pre_a] != b[suf_b]:
                break
            pre_a += 1
            suf_b -= 1
        if self.check(a[pre_a:suf_b + 1]) or self.check(b[pre_a:suf_b + 1]):
            return True

        pre_b, suf_a = 0, n - 1
        while pre_b < suf_a:
            if b[pre_b] != a[suf_a]:
                break
            pre_b += 1
            suf_a -= 1
        if self.check(a[pre_b:suf_a + 1]) or self.check(b[pre_b:suf_a + 1]):
            return True

        return False
