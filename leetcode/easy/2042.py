"""
tag: 字符串
2042. 检查句子中的数字是否递增
https://leetcode.cn/problems/check-if-numbers-are-ascending-in-a-sentence/
"""
import re


class Solution0:
    """ 正则表达式 re 模块 """
    def areNumbersAscending(self, s: str) -> bool:
        nums = re.findall(r'[0-9]+', s)
        nums = [int(n) for n in nums]
        # nums = [int(item) for item in s.split() if item.isdigit()]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
        return True


class Solution1:
    """ 正则表达式解决简单问题效率低 """
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(item) for item in s.split() if item.isdigit()]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
        return True


class Solution2:
    """ 全手动 """
    def areNumbersAscending(self, s: str) -> bool:
        pre = i = 0
        while i < len(s):
            if s[i].isdigit():
                cur = 0
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                if cur <= pre:
                    return False
                pre = cur
            else:
                i += 1
        return True
