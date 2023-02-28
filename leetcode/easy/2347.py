"""
tag: 数组；哈希表；计数
2347. 最好的扑克手牌
https://leetcode.cn/problems/best-poker-hand/
"""
from collections import Counter


class Solution0_Error:
    """ 错误范例
    [0, 1, 2, 1, 2] """
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        ranks_ = set(ranks)
        if len(set(suits)) == 1:
            return "Flush"
        elif len(ranks_) <= 3:
            return "Three of a Kind"
        elif len(ranks_) == 4:
            return "Pair"
        else:
            return "High Card"


class Solution0:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        else:
            ranks_ = Counter(ranks).most_common()[0][1]
            if ranks_ >= 3:
                return "Three of a Kind"
            elif ranks_ == 2:
                return "Pair"
            else:
                return "High Card"
