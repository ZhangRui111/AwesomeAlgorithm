"""
tag: 数组；回溯；矩阵
剑指 Offer 12. 矩阵中的路径
https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof/
"""
from collections import Counter
from functools import reduce


class Solution1:
    """ 官解 (使用 visited 矩阵避免重复访问) + 提前False优化 """
    def exist(self, board: List[List[str]], word: str) -> bool:

        # 提前False优化：效果显著
        board_cnt = Counter(reduce(lambda a, b: a + b, [*board]))
        word_cnt = Counter(word)
        if word_cnt - board_cnt:
            return False

        def check(i: int, j: int, k: int):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False
            if k == k_end_cond:
                return True

            visited.add((i, j))

            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if (new_i, new_j) not in visited:
                    if check(new_i, new_j, k + 1):
                        return True

            visited.remove((i, j))
            return False

        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        k_end_cond = len(word) - 1
        visited = set()
        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True

        return False


class Solution2:
    """ 官解 (修改 board 避免重复访问) + 提前False优化 """
    def exist(self, board: List[List[str]], word: str) -> bool:

        # 提前False优化：效果显著
        board_cnt = Counter(reduce(lambda a, b: a + b, [*board]))
        word_cnt = Counter(word)
        if word_cnt - board_cnt:
            return False

        def check(i: int, j: int, k: int):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False
            if k == k_end_cond:
                return True

            board[i][j] = ''

            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if check(new_i, new_j, k + 1):
                    return True

            board[i][j] = word[k]
            return False

        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        k_end_cond = len(word) - 1
        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True

        return False
