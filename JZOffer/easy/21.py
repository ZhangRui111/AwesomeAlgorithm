"""
tag: 数组；双指针；排序
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/?favorite=xb9nqhhg
"""


class Solution0_1:
    """ 双列表 """
    def exchange(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for n in nums:
            if n & 1:
                odd.append(n)
            else:
                even.append(n)
        return odd + even


class Solution0_2:
    """ 双指针 + 交换 """
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while nums[left] & 1 and left < right:
                left += 1
            while not nums[right] & 1 and left < right:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums
