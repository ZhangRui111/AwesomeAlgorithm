"""
tag: 二叉树；广度优先搜索
剑指 Offer 32 - III. 从上到下打印二叉树 III
https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/?favorite=xb9nqhhg
"""
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            level_size = len(q)
            level_res = []
            for _ in range(level_size):
                node = q.popleft()
                level_res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_res)
        res = [item[::-1] if i & 1 else item for i, item in enumerate(res)]
        return res
