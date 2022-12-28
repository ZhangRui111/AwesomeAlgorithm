"""
tag: 数组，矩阵
剑指 Offer 04. 二维数组中的查找
https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""


class Solution0:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # special case that must be considered, i.e., n = 0 or m = 0.
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row = 0
        right = len(matrix[0]) - 1  # 每行的最右搜索上界
        while row < len(matrix):
            nums = matrix[row]
            low, high = 0, right

            if nums[low] > target:  # 提前终止
                return False

            if nums[high] < target:
                row += 1  # error-prone point
                continue

            while nums[high] > target:
                high -= 1
                right -= 1  # key point
            if nums[high] == target:
                return True
            else:
                row += 1
        return False


class Solution1:
    """ 官解：Z 字形查找，与 Solution0 思路类似 """
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1  # 从右上角开始搜索
        while x < m and y >= 0:
            if matrix[x][0] > target:  # 提前终止
                return False

            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:  # 消去一列
                y -= 1
            else:  # 消去一行
                x += 1
        return False
