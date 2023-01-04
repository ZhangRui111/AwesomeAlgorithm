"""
tag: 数组；二分查找
剑指 Offer 11. 旋转数组的最小数字
https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
"""


class Solution0:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] == numbers[high]:  # special case
                if len(set(numbers[pivot: high + 1])) == 1:
                    high = pivot
                else:
                    low = pivot + 1
            else:
                low = pivot + 1
        return numbers[low]


class Solution1:
    """ 官解 """
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]
