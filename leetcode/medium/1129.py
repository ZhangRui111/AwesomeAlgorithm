"""
tag: 广度优先搜索；图
1129. 颜色交替的最短路径
https://leetcode.cn/problems/shortest-path-with-alternating-colors/
"""


class Solution:
    """ 官解 """
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 构建图，g[x] 表示从节点 x 出发可以到达的节点 y 以及 x 到 y 的路径类型
        g = [[] for _ in range(n)]
        for x, y in redEdges:
            g[x].append((y, 0))
        for x, y in blueEdges:
            g[x].append((y, 1))

        dis = [-1] * n
        vis = {(0, 0), (0, 1)}  # {(到达节点 0 的最后一段路径是红色),
                                #  (到达节点 0 的最后一段路径是蓝色)}
        q = [(0, 0), (0, 1)]  # 队列，含义同 vis
        level = 0
        while q:
            tmp = q
            q = []
            for x, color in tmp:
                if dis[x] == -1:
                    dis[x] = level
                for p in g[x]:
                    if p[1] != color and p not in vis:
                        vis.add(p)
                        q.append(p)
            level += 1
        return dis
