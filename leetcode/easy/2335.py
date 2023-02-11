"""
tag: 贪心；数组；排序；堆（优先队列）
2335. 装满杯子需要的最短总时长
https://leetcode.cn/problems/minimum-amount-of-time-to-fill-cups/
"""


class Solution0_1:
    """ 模拟：每次从最多的两杯开始倒水 """
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        while amount.count(0) < 1:
            if amount[0] == amount[1] == amount[2]:  # 必须步骤，不然可能 a == c
                res += (sum(amount) + 1) // 2
                return res
            a, c = amount.index(max(amount)), amount.index(min(amount))
            b = 3 - a - c
            target_b = max(0, amount[c] - 1)
            minus = amount[b] - target_b
            res += minus
            amount[a] -= minus
            amount[b] -= minus
        res += max(amount)
        return res


class Solution0_2:
    """ Solution0_1 微优化 """
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        while amount.count(0) < 1:
            amount.sort()
            if amount[0] == amount[2]:
                res += (sum(amount) + 1) // 2
                return res
            target_mid = max(0, amount[0] - 1)
            minus = amount[1] - target_mid
            res += minus
            amount[2] -= minus
            amount[1] -= minus
        res += max(amount)
        return res


class Solution1:
    """ 贪心 + 分类讨论
    思路：x <= y <= z，x 和 y 作为一组，跟 z 比较 """
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if amount[2] > amount[1] + amount[0]:
            return amount[2]
        return (sum(amount) + 1) // 2
