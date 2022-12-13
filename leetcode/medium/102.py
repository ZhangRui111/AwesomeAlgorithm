"""
tag: 树；广度优先搜索
102. 二叉树的层序遍历
https://leetcode.cn/problems/binary-tree-level-order-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            level_res = []
            for i in range(level_size):
                node = queue.popleft()
                level_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_res)
        return res
