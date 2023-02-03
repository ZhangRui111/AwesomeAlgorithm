"""
tag: 树；递归
226. 翻转二叉树
https://leetcode.cn/problems/invert-binary-tree/
"""

# 同 剑指 Offer 27. 二叉树的镜像 (easy)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root
