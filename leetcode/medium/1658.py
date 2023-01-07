"""
tag: 数组；前缀和；滑动窗口
1658. 将 x 减到 0 的最小操作数
https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/
"""
from typing import List


class Solution0_0:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 有可能存在多个解，选择其中最小的值
        # e.g., 测试示例: self.minOperations([5, 2, 3, 1, 1], 5)
        valid_ans = []

        # 问题转化为数组中寻找一个滑动窗口，使其和为 mid_target
        mid_target = sum(nums) - x
        if mid_target < 0:
            return -1
        if mid_target == 0:
            return len(nums)

        left, right = 0, 0  # 滑动窗口的双指针
        mid_sum = 0  # 滑动窗口的和

        end = len(nums)
        while left <= right < end:
            mid_sum += nums[right]
            while mid_sum >= mid_target and left <= right:
                if mid_sum == mid_target:
                    valid_ans.append(len(nums) - (right - left) - 1)
                mid_sum -= nums[left]
                left += 1
            right += 1

        return min(valid_ans) if valid_ans else -1


class Solution0_1:
    """ Solution0_0 + left_sum 来判断 early stop
    left_sum 本身的维护代价较大，在测试集的表现似乎得不偿失 """

    def minOperations(self, nums: List[int], x: int) -> int:
        self.valid_ans = []

        mid_target = sum(nums) - x
        if mid_target < 0:
            return -1
        if mid_target == 0:
            return len(nums)

        left, right = 0, 0
        mid_sum = 0

        left_sum = 0  # nums 中位于滑动窗口左边的数字之和

        end = len(nums)
        while left <= right < end:
            mid_sum += nums[right]
            while mid_sum >= mid_target and left <= right:
                if mid_sum == mid_target:
                    self.valid_ans.append(len(nums) - (right - left) - 1)
                mid_sum -= nums[left]
                self.early_stop(left_sum, x, nums[left])
                left += 1
            right += 1

        return self.check_valid_ans()

    def check_valid_ans(self):
        return min(self.valid_ans) if self.valid_ans else -1

    def early_stop(self, left_sum, x, val):
        left_sum += val
        if left_sum > x:
            return self.check_valid_ans()


class Solution0_3:
    """ Solution0_0 写法优化 """
    def minOperations(self, nums: List[int], x: int) -> int:
        # 有可能存在多个解，选择其中最小的值
        # e.g., 测试示例: self.minOperations([5, 2, 3, 1, 1], 5)
        valid_ans = []

        # 问题转化为数组中寻找一个滑动窗口，使其和为 mid_target
        mid_target = sum(nums) - x
        if mid_target < 0:
            return -1
        if mid_target == 0:
            return len(nums)

        left, right = 0, 0  # 滑动窗口的双指针
        mid_sum = 0  # 滑动窗口的和

        end = len(nums)
        while left <= right < end:
            mid_sum += nums[right]
            while mid_sum > mid_target:
                mid_sum -= nums[left]
                left += 1
            right += 1
            if mid_sum == mid_target:
                valid_ans.append(len(nums) - (right - left))

        return min(valid_ans) if valid_ans else -1


class Solution1:
    """ 思路相同 """
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1  # 全部移除也无法满足要求
        ans = -1  # 中间数组的长度
        left = s = 0
        for right, x in enumerate(nums):
            s += x
            while s > target:  # 缩小子数组长度
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        return -1 if ans < 0 else len(nums) - ans


# a = Solution0_0()
# a.minOperations([5, 2, 3, 1, 1], 5)
# a.minOperations(
#     [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993,
#      9904, 8819, 1231, 6309], 134365)
# a.minOperations([3, 2, 20, 1, 1, 3], 10)
