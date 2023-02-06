"""
tag: 二叉树；深度优先搜索
2331. 计算布尔二叉树的值
https://leetcode.cn/problems/evaluate-boolean-binary-tree/
"""
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution0:
    """ 递归 """
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.val in [0, 1]:
                return bool(node.val)

            if node.left.val not in [0, 1]:
                node.left.val = dfs(node.left)
            if node.right.val not in [0, 1]:
                node.right.val = dfs(node.right)
            if node.val == 2:
                return bool(node.left.val or node.right.val)
            else:
                return bool(node.left.val and node.right.val)

        return dfs(root)


class Solution1:
    """ 递归官解 """
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return root.val == 1
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)
