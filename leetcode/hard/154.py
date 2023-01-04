"""
tag: 数组；二分查找
154. 寻找旋转排序数组中的最小值 II
https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/
"""


# class Solution:
#     """ 153. 寻找旋转排序数组中的最小值 """
#     def findMin(self, nums: List[int]) -> int:
#         low, high = 0, len(nums) - 1
#         while low < high:
#             pivot = low + (high - low) // 2
#             if nums[pivot] < nums[high]:
#                 high = pivot
#             else:
#                 low = pivot + 1
#         return nums[low]


class Solution0:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            elif nums[pivot] == nums[high]:  # special case
                if len(set(nums[pivot: high + 1])) == 1:
                    high = pivot
                else:
                    low = pivot + 1
            else:
                low = pivot + 1
        return nums[low]


class Solution1:
    """ 官解 """
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
        return nums[low]
