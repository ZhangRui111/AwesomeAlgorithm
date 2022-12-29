"""
tag: 数组；哈希表
2032. 至少在两个数组中出现的值
https://leetcode.cn/problems/two-out-of-three/
"""


class Solution:
    """ set() """
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
        return list((nums1 & nums2) | (nums2 & nums3) | (nums1 & nums3))
