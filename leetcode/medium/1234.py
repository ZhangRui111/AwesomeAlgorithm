"""
tag: 字符串；滑动窗口
1234. 替换子串得到平衡字符串
https://leetcode.cn/problems/replace-the-substring-for-balanced-string/
"""
from collections import Counter


class Solution0:
    """ 超时
    思路：替换子串长度与字符串剩余部分的关系，即，
    sup_n = 4 * max_n - (q_n + w_n + e_n + r_n) """
    def balancedString(self, s: str) -> int:
        res = len_s = len(s)
        Q_cnt, W_cnt, E_cnt, R_cnt = s.count('Q'), s.count('W'), s.count(
            'E'), s.count('R')
        if Q_cnt == W_cnt == E_cnt == R_cnt:
            return 0

        for start in range(len_s):
            cnt = {
                'Q': 0,
                'W': 0,
                'E': 0,
                'R': 0,
            }
            for end in range(start, len_s):
                cnt[s[end]] += 1
                len_sup = end - start + 1
                if len_sup >= res:
                    break
                q_n = Q_cnt - cnt['Q']
                w_n = W_cnt - cnt['W']
                e_n = E_cnt - cnt['E']
                r_n = R_cnt - cnt['R']
                max_n = max(q_n, w_n, e_n, r_n)
                sup_n = 4 * max_n - (q_n + w_n + e_n + r_n)
                if len_sup == sup_n:
                    res = len_sup
                    break
                end += 1
        return res


class Solution1:
    """ 官解
    我们选择 s 的一个子串作为待替换子串，只有当 s 剩余部分中各字母的出现次数
    都小于等于 n/4 时，才可以使 s 变为平衡字符串 """
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        partial = len(s) // 4

        def check():
            if cnt['Q'] > partial or \
                    cnt['W'] > partial or \
                    cnt['E'] > partial or \
                    cnt['R'] > partial:
                return False
            return True

        if check():
            return 0

        res = len(s)
        right = 0
        for left, c in enumerate(s):
            while right < len(s) and not check():
                cnt[s[right]] -= 1
                right += 1
            if not check():
                break
            res = min(res, right - left)
            cnt[c] += 1
        return res
