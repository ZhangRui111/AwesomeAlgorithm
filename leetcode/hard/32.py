"""
tag: 栈；字符串；动态规划
32. 最长有效括号
https://leetcode.cn/problems/longest-valid-parentheses/
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        # 栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」;
        # 栈里其他元素维护左括号的下标
        stack = list()
        stack.append(-1)
        len_s = len(s)
        for i in range(len_s):
            if s[i] == "(":
                stack.append(i)
            else:  # s[i] == ")"
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length
