"""
tag: 贪心；数组
2383. 赢得比赛需要的最少训练时长
https://leetcode.cn/problems/minimum-hours-of-training-to-win-a-competition/
"""
from itertools import accumulate


class Solution0:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        energy_req = max(sum(energy) + 1 - initialEnergy, 0)
        experience_accum = list(
            accumulate([initialExperience] + experience))  # 额外的空间开支
        experience_req = max(
            max(a - b + 1 for a, b in zip(experience, experience_accum[:-1])),
            0)
        return energy_req + experience_req


class Solution1:
    """ 模拟 """
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        sm = sum(energy)
        trainingHours = 0 if initialEnergy > sm else sm + 1 - initialEnergy
        for e in experience:
            if initialExperience <= e:
                trainingHours += 1 + (e - initialExperience)
                initialExperience = 2 * e + 1
            else:
                initialExperience += e
        return trainingHours
