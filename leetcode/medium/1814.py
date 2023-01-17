"""
tag: 数组；哈希表；数学；计数
1814. 统计一个数组中好对子的数目
https://leetcode.cn/problems/count-nice-pairs-in-an-array/
"""
import math
from collections import Counter


class Solution0_1:
    """ a + rev(b) == rev(a) + b 等价于 a - rev(a) == b - rev(b) """
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            return int(str(n)[::-1])

        rev_nums = [rev(n) for n in nums]
        res = 0
        diff = [a - b for a, b in zip(nums, rev_nums)]
        diff_cnt = Counter(diff)
        for k, v in diff_cnt.items():
            if v == 2:
                res += 1
            if v > 2:
                res += math.comb(v, 2)
                # res = res % (10 ** 9 + 7)
        return res % (10 ** 9 + 7)


class Solution0_2:
    """ Solution0_1 优化 """
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            return int(str(n)[::-1])

        res = 0
        diff = [n - rev(n) for n in nums]
        diff_cnt = Counter(diff)
        for k, v in diff_cnt.items():
            if v == 2:
                res += 1
            if v > 2:
                res += int(v * (v - 1) / 2)  # i.e., math.comb(v, 2)
                # res = res % (10 ** 9 + 7)
        return res % (10 ** 9 + 7)


class Solution1:
    """ 官解，res += cnt[i - j] """
    def countNicePairs(self, nums: List[int]) -> int:
        res = 0
        cnt = Counter()
        for i in nums:
            j = int(str(i)[::-1])
            res += cnt[i - j]
            cnt[i - j] += 1
        return res % (10 ** 9 + 7)

