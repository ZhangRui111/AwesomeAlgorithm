"""
tag: 数组；矩阵
2319. 判断矩阵是否是一个 X 矩阵
https://leetcode.cn/problems/check-if-matrix-is-x-matrix/
"""


class Solution0:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        # 检查对角线并覆盖对角线为0
        n = len(grid)
        top_left, top_right, bottom_left, bottom_right = [0, 0], [0, n - 1], [
            n - 1, 0], [n - 1, n - 1]
        while top_left[1] <= top_right[1] and top_left[0] <= bottom_left[0]:
            if top_left == top_right == bottom_left == bottom_right:
                if grid[top_left[0]][top_left[1]] == 0:
                    return False
                grid[top_left[0]][top_left[1]] = 0
            else:
                for pos in [top_left, top_right, bottom_left, bottom_right]:
                    if grid[pos[0]][pos[1]] == 0:
                        return False
                    grid[pos[0]][pos[1]] = 0
            top_left[0] += 1
            top_left[1] += 1
            top_right[0] += 1
            top_right[1] -= 1
            bottom_left[0] -= 1
            bottom_left[1] += 1
            bottom_right[0] -= 1
            bottom_right[1] -= 1

        # 由于对角线合规并且被覆盖为0，只需检查grid是否有不为0的值即可
        for row in grid:
            if any(row):
                return False
        return True


class Solution1:
    """ 官解 """
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i == j or (i + j) == (n - 1):
                    if x == 0:
                        return False
                elif x:
                    return False
        return True


class Solution2:
    """ 评论区代码简化
    像这种需要判断「两个条件都为真」「两个条件都为假」的逻辑，都可以直接用这两个条件
    的 bool 值作比较，从而简化代码逻辑 """
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if (x == 0) == (i == j or i + j == len(grid) - 1):
                    return False
        return True
