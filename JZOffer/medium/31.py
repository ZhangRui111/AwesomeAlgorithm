"""
tag: 栈；数组；模拟
剑指 Offer 31. 栈的压入、弹出序列
https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/?favorite=xb9nqhhg
"""


class Solution0:
    """ 模拟 """
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for v in popped:
            try:
                v_idx = stack.index(v)
                stack = stack[:v_idx]
            except ValueError:
                try:
                    v_idx = pushed.index(v)
                except ValueError:
                    return False  # 栈里和还未入栈的都找不到，说明早就弹出了
                stack += pushed[:v_idx]
                pushed = pushed[v_idx + 1:]
        return True


class Solution1:
    """ 官解 """
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st, j = [], 0
        for x in pushed:
            st.append(x)
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
        return len(st) == 0
