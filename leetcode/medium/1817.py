"""
tag: 数组；哈希表
1817. 查找用户活跃分钟数
https://leetcode.cn/problems/finding-the-users-active-minutes/
"""
from collections import defaultdict, Counter


class Solution0_1:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user = defaultdict(list)
        for item in logs:
            user[item[0]].append(item[1])
        user_cnt = Counter([len(set(v)) for k, v in user.items()])
        res = [0] * k
        for i in range(k):
            res[i] = user_cnt[i + 1]
        return res


class Solution0_2:
    """ 优化 (时空优化效果一般) """
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user = defaultdict(set)
        for i, o in logs:
            user[i].add(o)
        user_cnt = Counter([len(v) for v in user.values()])
        res = [0] * k
        for i in range(k):
            res[i] = user_cnt[i + 1]
        return res


class Solution1:
    """ 官解，快多了 """
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mp = defaultdict(set)
        for i, t in logs:
            mp[i].add(t)
        ans = [0] * k
        for s in mp.values():
            ans[len(s) - 1] += 1
        return ans
