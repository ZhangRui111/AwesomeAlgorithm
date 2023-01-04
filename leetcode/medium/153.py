"""
tag: 数组；二分查找
153. 寻找旋转排序数组中的最小值
https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
"""


class Solution0_0:
    """ 可行的方案，但是
    (1) 没有考虑到数组的递增性质，因此递归条件选的不好
    (2) 递归形式的二分查找可读性差，且占用更多空间 """
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        def binary_search(low, high):
            mid = (low + high) // 2
            if low == mid:
                return min(nums[low], nums[high])
            if nums[low] <= nums[mid]:  # 有待优化
                return binary_search(mid, high)
            else:
                return binary_search(low, mid)

        low, high = 0, len(nums) - 1
        return binary_search(low, high)


class Solution0_1:
    """ 优化迭代条件 """
    def findMin(self, nums: List[int]) -> int:
        def binary_search(low, high):
            mid = (low + high) // 2
            if low == mid:
                return min(nums[low], nums[high])
            if nums[mid] < nums[high]:  # 考虑数组递增的优化
                return binary_search(low, mid)
            else:
                return binary_search(mid + 1, high)

        low, high = 0, len(nums) - 1
        return binary_search(low, high)


class Solution0_2:
    """ 优化终止条件，官解的等价版本但更低效 """
    def findMin(self, nums: List[int]) -> int:
        def binary_search(low, high):
            if low == high:
                return nums[low]
            mid = low + (high - low) // 2  # 避免 (low + high) 溢出
            if nums[mid] < nums[high]:
                return binary_search(low, mid)
            else:
                return binary_search(mid + 1, high)

        low, high = 0, len(nums) - 1
        return binary_search(low, high)


class Solution1:
    """ 官解 """
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]
