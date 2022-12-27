"""
tag: 数组；哈希表；排序
剑指 Offer 03. 数组中重复的数字
https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/?favorite=xb9nqhhg
"""


class Solution1:
    def findRepeatNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ht = [-1] * n
        for val in nums:
            if ht[val] == -1:
                ht[val] = val
            else:
                return val
        return -1


class Solution2:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]  # Error
            #
            # Python 中， a, b = c, d 操作的原理是先暂存元组 (c, d)，
            # 然后 “按左右顺序” 赋值给 a 和 b 。
            # 因此，若写为 nums[i], nums[nums[i]] = nums[nums[i]], nums[i] ，
            # 则 nums[i] 会先被赋值，之后 nums[nums[i]] 指向的元素则会出错。
        return -1
