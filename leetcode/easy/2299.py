"""
tag: 字符串
2299. 强密码检验器 II
https://leetcode.cn/problems/strong-password-checker-ii/
"""


class Solution0:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        special_chars = "!@#$%^&*()-+"
        flags = [False] * 4
        for i, c in enumerate(password):
            if i == 0:
                pre_c = c
            else:
                if pre_c == c:
                    return False
                pre_c = c

            if sum(flags) < 4:
                if c in special_chars:
                    flags[3] = True
                elif '0' <= c <= '9':
                    flags[2] = True
                elif 'A' <= c <= 'Z':
                    flags[1] = True
                elif 'a' <= c <= 'z':
                    flags[0] = True
                else:
                    return False

        return True if sum(flags) == 4 else False


class Solution1:
    """ 优化 """
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        special_chars = "!@#$%^&*()-+"
        hasLower = hasUpper = hasDigit = hasSpecial = False
        for i, c in enumerate(password):
            if i > 0 and password[i] == password[i - 1]:
                return False

            if c in special_chars:
                hasSpecial = True
            elif c.isdigit():
                hasDigit = True
            elif c.isupper():
                hasUpper = True
            elif c.islower():
                hasLower = True
            else:
                return False

        return hasLower and hasUpper and hasDigit and hasSpecial
