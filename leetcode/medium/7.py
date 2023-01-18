"""
tag: 数学
7. 整数反转
https://leetcode.cn/problems/reverse-integer/
"""


class Solution0:
    """ Shortcut 解法  """
    def reverse(self, x: int) -> int:
        def rev(n):
            return int(str(n)[::-1])
        x = rev(x) if x >= 0 else -rev(-x)
        return x if -2**31 <= x <= 2**31 - 1 else 0


class Solution1:
    """ 官解 """
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0

            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit

        return rev
