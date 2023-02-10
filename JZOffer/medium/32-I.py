"""
tag: 二叉树；广度优先搜索
剑指 Offer 32 - I. 从上到下打印二叉树
https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/?favorite=xb9nqhhg
"""
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
