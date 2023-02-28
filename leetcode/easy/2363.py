"""
tag: 数组；哈希表；有序集合；排序
2363. 合并相似的物品
https://leetcode.cn/problems/merge-similar-items/
"""
from collections import Counter


class Solution0:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = sorted(items1 + items2, key=lambda item: item[0])
        len_items = len(items)
        res = []
        idx = 0
        while idx < len_items:
            if idx < len_items - 1 and items[idx][0] == items[idx + 1][0]:
                res.append([items[idx][0], items[idx][1] + items[idx + 1][1]])
                idx += 1
            else:
                res.append([items[idx][0], items[idx][1]])
            idx += 1
        return res


class Solution1:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        """ better """
        res = Counter()
        for a, b in items1:
            res[a] += b
        for a, b in items2:
            res[a] += b
        return sorted([a, b] for a, b in res.items())
