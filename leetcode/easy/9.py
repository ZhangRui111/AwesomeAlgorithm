"""
tag: 数学
9. 回文数
https://leetcode.cn/problems/palindrome-number/
"""


class Solution0:
    """ Pythonic solution """
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x == 0:
            return True

        if x % 10 == 0:
            return False

        reverted_x = 0
        while x > reverted_x:
            reverted_x = reverted_x * 10 + x % 10
            x = x // 10

        return x == reverted_x or x == reverted_x // 10
