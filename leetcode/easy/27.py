"""
tag: 数组；双指针
27. 移除元素
https://leetcode.cn/problems/remove-element/
"""


class Solution1:
    """ My solution: 头尾双指针 + 交换 """
    def removeElement(self, nums: List[int], val: int) -> int:
        head, tail = 0, len(nums) - 1
        while head <= tail:
            if nums[head] == val:
                # 确保交换的元素不等于val
                while tail > head and nums[tail] == val:
                    tail -= 1
                if tail <= head:
                    break
                self.swap(nums, head, tail)
            head += 1
        return head

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


class Solution2:
    """ 头尾双指针（优化） """
    def removeElement(self, nums: List[int], val: int) -> int:
        head, tail = 0, len(nums)
        while head < tail:
            if nums[head] == val:
                # 不确保交换的元素不等于val
                nums[head] = nums[tail - 1]
                tail -= 1
            else:
                head += 1
        return head


class Solution3:
    """ head双指针 + 覆盖 """
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        len_nums = len(nums)
        for j in range(len_nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
