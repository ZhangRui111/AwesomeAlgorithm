"""
tag: 哈希表；字符串；计数
2283. 判断一个数的数字计数是否等于数位的值
https://leetcode.cn/problems/check-if-number-has-equal-digit-count-and-digit-value/
"""
from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        num = [int(c) for c in num]
        num_cnt = Counter(num)
        for idx, val in enumerate(num):
            if val != num_cnt[idx]:
                return False
        return True
