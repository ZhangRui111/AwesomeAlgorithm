"""
tag: 贪心；数组；二分查找；前缀和；排序
2389. 和有限的最长子序列
https://leetcode.cn/problems/longest-subsequence-with-limited-sum/
"""
from itertools import accumulate
from bisect import bisect_right


class Solution0:
    """ 排序 + 前缀和 + 恢复有序数组 """
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        len_nums = len(nums)
        pre_nums = list(accumulate(sorted(nums)))  # 前缀和
        len_queries = len(queries)
        queries_sorted = sorted(queries)

        answer_sorted, idx = [], 0
        for q in queries_sorted:
            while idx < len_nums and q >= pre_nums[idx]:
                idx += 1
            if idx == len_nums:
                break
            answer_sorted.append(idx)
        while len(answer_sorted) < len_queries:
            answer_sorted.append(len_nums)

        # unsort the answer_sorted:
        # queries_sorted --> answer_sorted
        #        queries --> answer
        queries_sorted_idx = sorted(range(len_queries), key=queries.__getitem__)
        answer = [None] * len_queries
        for val, idx in zip(answer_sorted, queries_sorted_idx):
            answer[idx] = val

        return answer


class Solution1:
    """ 排序 + 前缀和 + 二分查找 """
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        f = list(accumulate(sorted(nums)))
        return [bisect_right(f, q) for q in queries]

