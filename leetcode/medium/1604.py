"""
tag: 数组；哈希表；字符串；排序
1604. 警告一小时内使用相同员工卡大于等于三次的人
https://leetcode.cn/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
"""
from collections import defaultdict


class Solution0:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        keyName_defaultDict = defaultdict(list)
        for n, t in zip(keyName, keyTime):
            keyName_defaultDict[n].append(t)

        def check(times: List[str]):
            times.sort()
            if len(times) < 3:
                return False
            for i in range(0, len(times) - 2):
                left, right = times[i], times[i + 2]
                left_hour, left_min = left.split(':')
                right_hour, right_min = right.split(':')
                if right_hour == left_hour or int(right_hour) - 1 == int(
                        left_hour) and right_min <= left_min:
                    return True
            return False

        res = []
        for name, times in dict(keyName_defaultDict).items():
            if check(times):
                res.append(name)
        return sorted(res)


class Solution1:
    """ 官解 """
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        timeMap = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, minute = int(time[:2]), int(time[3:])
            timeMap[name].append(hour * 60 + minute)

        ans = []
        for name, times in timeMap.items():
            times.sort()
            if any(t2 - t1 <= 60 for t1, t2 in zip(times, times[2:])):
                ans.append(name)
        ans.sort()
        return ans
