"""
tag: 数组；字符串
2185. 统计包含给定前缀的字符串
https://leetcode.cn/problems/counting-words-with-a-given-prefix/
"""


class Solution0:
    """ 利用 Python 切片可以优雅处理部分无意义切片的特性 """
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        len_pref = len(pref)
        for word in words:
            if word[:len_pref] == pref:
                cnt += 1
        return cnt


class Solution1:
    """ 官解 """
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)
