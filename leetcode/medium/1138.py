"""
tag: 哈希表；字符串
1138. 字母板上的路径
https://leetcode.cn/problems/alphabet-board-path/
"""


class Solution0_1:
    def alphabetBoardPath(self, target: str) -> str:
        target_item_idx = {
            'a': (0, 0),
            'b': (0, 1),
            'c': (0, 2),
            'd': (0, 3),
            'e': (0, 4),
            'f': (1, 0),
            'g': (1, 1),
            'h': (1, 2),
            'i': (1, 3),
            'j': (1, 4),
            'k': (2, 0),
            'l': (2, 1),
            'm': (2, 2),
            'n': (2, 3),
            'o': (2, 4),
            'p': (3, 0),
            'q': (3, 1),
            'r': (3, 2),
            's': (3, 3),
            't': (3, 4),
            'u': (4, 0),
            'v': (4, 1),
            'w': (4, 2),
            'x': (4, 3),
            'y': (4, 4),
            'z': (5, 0),
        }
        pos = [0, 0]
        res = []
        for item in target:
            if item != 'z' and pos == (5, 0):
                res.append('U')
                pos = [4, 0]
            if item == 'z' and pos[1] != 0:
                res.append('L' * pos[1])
                pos = [pos[0], 0]
            target_pos = target_item_idx[item]
            x = target_pos[0] - pos[0]
            y = target_pos[1] - pos[1]
            if x < 0:
                res.append('U' * -x)
            else:
                res.append('D' * x)
            if y < 0:
                res.append('L' * -y)
            else:
                res.append('R' * y)
            res.append('!')
            pos = target_pos
        return "".join(res)


class Solution1:
    """ 官解 """
    def alphabetBoardPath(self, target: str) -> str:
        cx = cy = 0
        res = []
        for c in target:
            c = ord(c) - ord('a')
            nx = c // 5
            ny = c % 5
            if nx < cx:
                res.append('U' * (cx - nx))
            if ny < cy:
                res.append('L' * (cy - ny))
            if nx > cx:
                res.append('D' * (nx - cx))
            if ny > cy:
                res.append('R' * (ny - cy))
            res.append('!')
            cx = nx
            cy = ny
        return ''.join(res)


class Solution0_2:
    """ Solution0_1 优化 """
    def alphabetBoardPath(self, target: str) -> str:
        target_item_idx = {
            'a': (0, 0),
            'b': (0, 1),
            'c': (0, 2),
            'd': (0, 3),
            'e': (0, 4),
            'f': (1, 0),
            'g': (1, 1),
            'h': (1, 2),
            'i': (1, 3),
            'j': (1, 4),
            'k': (2, 0),
            'l': (2, 1),
            'm': (2, 2),
            'n': (2, 3),
            'o': (2, 4),
            'p': (3, 0),
            'q': (3, 1),
            'r': (3, 2),
            's': (3, 3),
            't': (3, 4),
            'u': (4, 0),
            'v': (4, 1),
            'w': (4, 2),
            'x': (4, 3),
            'y': (4, 4),
            'z': (5, 0),
        }
        pos_x, pos_y = 0, 0  # 节省索引的时间
        res = []
        for item in target:
            target_pos_x, target_pos_y = target_item_idx[item]
            # 节省处理 special case 的时间
            x = target_pos_x - pos_x
            y = target_pos_y - pos_y
            if x < 0:
                res.append('U' * -x)
            if y < 0:
                res.append('L' * -y)
            if x > 0:
                res.append('D' * x)
            if y > 0:
                res.append('R' * y)
            res.append('!')
            pos_x, pos_y = target_pos_x, target_pos_y
        return "".join(res)
