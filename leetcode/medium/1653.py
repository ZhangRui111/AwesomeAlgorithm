"""
tag: 栈；字符串；动态规划
1653. 使字符串平衡的最少删除次数
https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/
"""


class Solution0:
    """ 动态规划/滑动窗口 """
    def minimumDeletions(self, s: str) -> int:
        cnt_left_b, cnt_right_a = 0, s.count('a')
        ans = cnt_right_a
        for c in s:
            if c == 'b':
                cnt_left_b += 1
            else:
                cnt_right_a -= 1
            ans = min(ans, cnt_left_b + cnt_right_a)
        return ans

