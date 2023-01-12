"""
tag: 字符串
剑指 Offer 20. 表示数值的字符串
https://leetcode.cn/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/?favorite=xb9nqhhg
"""
import re


class Solution0_1:
    def isNumber(self, s: str) -> bool:
        pat = r"\s*"\
              r"[+-]?((\d+\.\d*)|(\d*\.\d+)|(\d+)){1}"\
              r"([eE][+-]?\d+)?"\
              r"\s*"
        try:
            return re.match(pat, s).group() == s
        except AttributeError:
            return False


class Solution0_2:
    """ 优化：
    加入 ^$ 匹配开头结尾，即尝试匹配整个字符串，匹配结果只有两种 """
    def isNumber(self, s: str) -> bool:
        pat = r"^\s*" \
              r"[+-]?((\d+\.\d*)|(\d*\.\d+)|(\d+)){1}" \
              r"([eE][+-]?\d+)?" \
              r"\s*$"
        return bool(re.match(pat, s))

# # debug
# s = Solution0_2()
#
# for i in ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]:
#     print(s.isNumber(i), end=", ")
# print()
# for i in ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]:
#     print(s.isNumber(i), end=", ")
# print()
#
# print(s.isNumber("+100"))
# print(s.isNumber(" "))
# print(s.isNumber("e9"))
