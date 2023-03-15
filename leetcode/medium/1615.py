"""
tag: 图
1615. 最大网络秩
https://leetcode.cn/problems/maximal-network-rank/
"""
from functools import reduce
from collections import Counter, defaultdict


class Solution0_Error:
    """ 两个城市不必相连
    输入：
    8
    [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    输出：
    4
    预期结果：
    5
    """
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        roads_ = reduce(lambda a, b: a + b, roads)
        roads_cnt = Counter(roads_)
        res = 0
        for r in roads:
            res = max(roads_cnt[r[0]] + roads_cnt[r[1]] - 1, res)
        return res


class Solution0_1:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:  # special case
            return 0

        roads_ = reduce(lambda a, b: a + b, roads)
        roads_cnt = Counter(roads_)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                # if [i, j] in roads:  # error
                if [i, j] in roads or [j, i] in roads:
                    res = max(roads_cnt[i] + roads_cnt[j] - 1, res)
                else:
                    res = max(roads_cnt[i] + roads_cnt[j], res)
        return res


class Solution0_2:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:  # special case
            return 0

        # road counter
        roads_ = reduce(lambda r1, r2: r1 + r2, roads)
        roads_cnt = Counter(roads_)

        # first round filter
        most_vs, first_second_roads, idx = [], {}, 0
        while True:
            try:
                k, v = roads_cnt.most_common()[idx]
            except IndexError:
                break
            if v not in most_vs:
                if len(most_vs) == 2:
                    break
                else:
                    most_vs.append(v)
            first_second_roads[k] = v
            idx += 1

        # for loop to obtain the answer
        res = 0
        for r1 in first_second_roads:
            for r2 in first_second_roads:
                if r1 != r2:
                    if [r1, r2] in roads or [r2, r1] in roads:
                        res = max(first_second_roads[r1] +
                                  first_second_roads[r2] - 1, res)
                    else:
                        res = max(first_second_roads[r1] +
                                  first_second_roads[r2], res)
        return res


class Solution0_2_:
    """ Solution0_2 without Counter
    faster & less space """
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:  # special case
            return 0

        # road counter
        roads_cnt = defaultdict(int)
        for a, b in roads:
            roads_cnt[a] += 1
            roads_cnt[b] += 1
        roads_cnt = sorted(dict(roads_cnt).items(), key=lambda item: item[1],
                           reverse=True)

        # first round filter
        most_vs, first_second_roads, idx = [], {}, 0
        while True:
            try:
                k, v = roads_cnt[idx]
            except IndexError:
                break
            if v not in most_vs:
                if len(most_vs) == 2:
                    break
                else:
                    most_vs.append(v)
            first_second_roads[k] = v
            idx += 1

        # for loop to obtain the answer
        res = 0
        for r1 in first_second_roads:
            for r2 in first_second_roads:
                if r1 != r2:
                    if [r1, r2] in roads or [r2, r1] in roads:
                        res = max(first_second_roads[r1] +
                                  first_second_roads[r2] - 1, res)
                    else:
                        res = max(first_second_roads[r1] +
                                  first_second_roads[r2], res)
        return res


class Solution1_1:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connect = [[False] * n for _ in range(n)]  # connect 数组十分关键
        degree = [0] * n
        for a, b in roads:
            connect[a][b] = True
            connect[b][a] = True
            degree[a] += 1
            degree[b] += 1

        maxRank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j] - connect[i][j]
                maxRank = max(maxRank, rank)
        return maxRank


class Solution1_2:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connect = [[False] * n for _ in range(n)]
        degree = defaultdict(int)
        for a, b in roads:
            connect[a][b] = True
            connect[b][a] = True
            degree[a] += 1
            degree[b] += 1
        degree = sorted(dict(degree).items(), key=lambda item: item[1],
                        reverse=True)

        most_vs, first_second_roads, idx = [], {}, 0
        while True:
            try:
                k, v = degree[idx]
            except IndexError:
                break
            if v not in most_vs:
                if len(most_vs) == 2:
                    break
                else:
                    most_vs.append(v)
            first_second_roads[k] = v
            idx += 1
        first_roads = {k: v for k, v in first_second_roads.items()
                       if v == degree[0][1]}

        # for loop to obtain the answer
        res = 0
        for r1 in first_roads:
            for r2 in first_second_roads:
                if r1 != r2:
                    res = max(
                        first_roads[r1] + first_second_roads[r2]
                        - connect[r1][r2], res)

        return res
