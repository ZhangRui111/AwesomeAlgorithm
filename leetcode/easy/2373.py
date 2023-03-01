"""
tag: 数组；矩阵
2373. 矩阵中的局部最大值
https://leetcode.cn/problems/largest-local-values-in-a-matrix/
"""


class Solution0:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        for i in range(n - 2):
            level_res = []
            for j in range(n - 2):
                level_res.append(max(
                    max(grid[i][j:j+3]),
                    max(grid[i+1][j:j+3]),
                    max(grid[i+2][j:j+3])
                ))
            res.append(level_res)
        return res

