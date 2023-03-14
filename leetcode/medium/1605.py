"""
tag: 贪心；数组；矩阵
1605. 给定行和列的和求可行矩阵
https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums/
"""


class Solution:
    """ 贪心 + 遍历
    matrix[i][j] = min(rowSum[i], colSum[j])，
    然后将 rowSum[i] 和 colSum[j] 同时减去 matrix[i][j]，
    遍历一遍后即得到一个满足条件的矩阵。
    同时注意 0 值出现后的 early stop
    """
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        matrix = [[0] * m for _ in range(n)]
        i = j = 0
        while i < n and j < m:
            v = min(rowSum[i], colSum[j])
            matrix[i][j] = v
            rowSum[i] -= v
            colSum[j] -= v
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        return matrix
