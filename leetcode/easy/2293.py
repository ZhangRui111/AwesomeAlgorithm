"""
tag: 数组；模拟
2293. 极大极小游戏
https://leetcode.cn/problems/min-max-game/
"""


class Solution0:
    def minMaxGame(self, nums: List[int]) -> int:
        while True:
            n = len(nums)
            if n == 1:
                return nums[0]
            new_n = n // 2
            new_nums = []
            for idx in range(new_n):
                if idx & 1:
                    new_nums.append(max(nums[2 * idx], nums[2 * idx + 1]))
                else:
                    new_nums.append(min(nums[2 * idx], nums[2 * idx + 1]))
            nums = new_nums
