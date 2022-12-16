"""
tag: 哈希表；字符串；计数
1781. 所有子字符串美丽值之和
https://leetcode.cn/problems/sum-of-beauty-of-all-substrings/
"""
from collections import Counter


class Solution1:
    """ 超时 (计数操作太过频繁) """
    def beautySum(self, s: str) -> int:
        n_s = len(s)
        if n_s <= 1:
            return 0

        res = 0
        subs = [s[start: start + sub_len + 1] for sub_len in range(1, n_s + 1)
                for start in range(n_s - sub_len)]
        for sub in subs:
            res += self.beauty(sub)
        return res

    def beauty(self, s: str):
        cnt = Counter(s).most_common()
        return cnt[0][1] - cnt[-1][1]


class Solution2:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            cnt = Counter()
            mx = 0
            for j in range(i, len(s)):
                cnt[s[j]] += 1
                mx = max(mx, cnt[s[j]])
                res += mx - min(cnt.values())
        return res
