"""
tag: 数组；矩阵；模拟
剑指 Offer 29. 顺时针打印矩阵
https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/?favorite=xb9nqhhg
"""


class Solution0:
    """ 撞墙就变向，同官解的一种解法 """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == [] or matrix == [[]]:
            return []

        m, n = len(matrix), len(matrix[0])
        pos = [[1] * n for _ in range(m)]
        # directions = ['right', 'down', 'left', 'up']
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        i, j, d = 0, 0, 0
        while True:
            if pos[i][j]:
                res.append(matrix[i][j])
                pos[i][j] = 0
            next_i, next_j = i + directions[d][0], j + directions[d][1]
            if next_i >= m or next_j >= n or not pos[next_i][next_j]:  # 撞墙变向
                d = (d + 1) % 4
                next_i, next_j = i + directions[d][0], j + directions[d][1]
                if next_i >= m or next_j >= n or not pos[next_i][next_j]:
                    break  # 变向后还是撞墙，到达终点了
            i, j = next_i, next_j
        return res


class Solution1:
    """ 官解：按层遍历 """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order
