"""
tag: 贪心；数组
1798. 你能构造出连续值的最大数目
https://leetcode.cn/problems/maximum-number-of-consecutive-values-you-can-make/
"""
from collections import Counter


class Solution0_1:
    """ 正确但超时 """
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins_cnt = Counter(coins)
        val, dp = 0, [[], ]
        while True:
            val += 1
            # print(val)
            if coins_cnt[val] > 0:
                dp.append([val])
            else:
                flag = False
                for i, item in enumerate(dp[::-1]):
                    if (coins_cnt - Counter(item))[i + 1] > 0:
                        dp.append(item + [i + 1])
                        flag = True
                        break
                if not flag:
                    return val


class Solution0_2:
    """ 相同的思路，比 Solution0_1 快一些，但是依然不够 """
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins_cnt = Counter(coins)
        val, dp = 0, [[], ]
        while True:
            val += 1
            # print(val)
            if coins_cnt[val] > 0:
                dp.append([val])
            else:
                flag = False
                for i, item in enumerate(dp[::-1]):
                    if coins_cnt[i + 1] - item.count(i + 1) > 0:
                        dp.append(item + [i + 1])
                        flag = True
                        break
                if not flag:
                    return val


class Solution1:
    """ 官解 """
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        x = 1
        for item in coins:
            if item > x:
                break
            x += item
        return x


# # 测试用例
# a = Solution0()
# res = a.getMaximumConsecutive([1,1,1,596,266,210,766,579,1,195,1,1,230,1,465,1,1,1,538,1,1,125,624,62,239,1,1,1,1,874,1,307,186,1,1,879,1,933,681,680,1,1,1,757,1,903,975,104,1,742,516,1,541,1,1,1,661,529,628,721,1,1,38,493,434,813,270,380,1,1,1,448,226,1,1,1,1,1,360,1,411,699,717,1,1,483,1,1,1,1,1,1,427,1,931,857,871,1,96,1,1,556,898,1,1,1,1,873,1,608,1,515,134,1,1,606,780,863,1,1,1,774,87,639,1,1,209,1,394,1,1,864,1,395,737,523,1,348,1,328,1,16,1,1,1,1,1,210,789,729,1,713,1,614,64,429,1,1,241,866,541,324])
# print(res)  # 预期结果：42215
