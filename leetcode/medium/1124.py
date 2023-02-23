"""
tag: 栈；数组；哈希表；前缀和；单调栈
1124. 表现良好的最长时间段
https://leetcode.cn/problems/longest-well-performing-interval/
"""

# https://leetcode.cn/problems/longest-well-performing-interval/solution/liang-chong-zuo-fa-liang-zhang-tu-miao-d-hysl/


class Solution1_1:
    """ 单调栈 + 前缀和 """
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        s = [0] * (n + 1)  # 前缀和
        st = [0]  # s[0] 单调栈
        for j, h in enumerate(hours, 1):
            s[j] = s[j - 1] + (1 if h > 8 else -1)
            if s[j] < s[st[-1]]:
                st.append(j)  # 感兴趣的索引 j --> 单调递减栈
        ans = 0
        for i in range(n, 0, -1):
            while st and s[i] > s[st[-1]]:
                ans = max(ans, i - st.pop())  # [st[-1],i) 可能是最长子数组
        return ans


class Solution1_2:
    """ 利用本题二值化后前缀和的连续性 """
    def longestWPI(self, hours: List[int]) -> int:
        pos = [0] * (len(hours) + 2)  # 记录前缀和首次出现的位置
        ans = s = 0  # s: 前缀和
        for i, h in enumerate(hours, 1):
            s += 1 if h > 8 else -1
            if s > 0:
                ans = i
            else:
                if pos[s - 1]:
                    ans = max(ans, i - pos[s - 1])  # 这里手写 if 会更快
                if pos[s] == 0:
                    pos[s] = i
        return ans
