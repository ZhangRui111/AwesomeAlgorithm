"""
tag: 哈希表；字符串；计数
2287. 重排字符形成目标字符串
https://leetcode.cn/problems/rearrange-characters-to-make-target-string/
"""
from collections import Counter
from math import inf


class Solution0:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_cnt = Counter(s)
        target_cnt = Counter(target)
        res = len(s)
        for item in target_cnt.keys():
            if item not in s_cnt.keys():
                return 0
            res = min(res, s_cnt[item] // target_cnt[item])
        return res


class Solution1:
    """ Solution0 优化 """
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_cnt = Counter(s)
        target_cnt = Counter(target)
        res = inf
        for c, n_c in target_cnt.items():
            res = min(res, s_cnt[c] // n_c)
            if res == 0:  # early stop
                return 0
        return res
