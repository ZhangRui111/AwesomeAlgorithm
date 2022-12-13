"""
tag: 哈希表，数学，字符串
12. 整数转罗马数字
https://leetcode.cn/problems/integer-to-roman/
"""


class Solution1:
    """ My solution """
    def intToRoman(self, num: int) -> str:
        n_m = num // 1000
        n_d = (num % 1000) // 500
        n_c = (num % 500) // 100
        n_l = (num % 100) // 50
        n_x = (num % 50) // 10
        n_v = (num % 10) // 5
        n_i = num % 5
        res = ""
        res = res + 'M' * n_m
        res = res + 'D' * n_d
        res = res + 'C' * n_c
        res = res + 'L' * n_l
        res = res + 'X' * n_x
        res = res + 'V' * n_v
        res = res + 'I' * n_i

        res = res.replace("VIIII", "IX")
        res = res.replace("IIII", "IV")
        res = res.replace("LXXXX", "XC")
        res = res.replace("XXXX", "XL")
        res = res.replace("DCCCC", "CM")
        res = res.replace("CCCC", "CD")

        return res


class Solution:
    """ My solution 2 (better!) """
    def intToRoman(self, num: int) -> str:
        table = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }
        res = ""
        for c, n in table.items():
            d, num = divmod(num, n)
            res += c * d
        return res
