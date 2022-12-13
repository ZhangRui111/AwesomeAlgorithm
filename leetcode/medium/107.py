"""
tag: 树；广度优先搜索
107. 二叉树的层序遍历 II
https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_res = []
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                level_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_res)

        res.reverse()

        return res
