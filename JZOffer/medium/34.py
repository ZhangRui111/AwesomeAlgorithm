"""
tag: 二叉树；深度优先搜索；回溯
剑指 Offer 34. 二叉树中和为某一值的路径
https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/?favorite=xb9nqhhg
"""
from collections import defaultdict, deque


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution0:
    """ 深度优先搜索 """
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []

        def dfs(node, target_n):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right:
                if node.val == target_n:
                    res.append(path[:])
                    # res.append(path)  # Error: 添加的是指向 path 的引用

            dfs(node.left, target_n - node.val)
            dfs(node.right, target_n - node.val)

            path.pop()  # 回溯
            # path = path[:-1]  # Error: 把全局变量转化为了局部变量

        res, path = [], []
        dfs(root, target)
        return res


class Solution1:
    """ 深度优先搜索 (写法优化) """
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:

        def dfs(node, target_n):
            if not node:
                return

            path.append(node.val)
            target_n -= node.val

            if not node.left and not node.right and target_n == 0:
                res.append(path[:])

            dfs(node.left, target_n)
            dfs(node.right, target_n)

            path.pop()

        res, path = [], []
        dfs(root, target)
        return res


class Solution2:
    """ 广度优先搜索 """
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        parent = defaultdict(lambda: None)  # 记录节点的父节点

        def get_path(node: TreeNode):
            path = []
            while node:
                path.append(node.val)
                node = parent[node]
            res.append(path[::-1])

        if not root:
            return []

        q_nodes = deque([root])
        q_vals = deque([root.val])
        while q_nodes:
            node = q_nodes.popleft()
            val = q_vals.popleft()

            if not node.left and not node.right:
                if val == target:
                    get_path(node)

            if node.left:
                parent[node.left] = node
                q_nodes.append(node.left)
                q_vals.append(val + node.left.val)
            if node.right:
                parent[node.right] = node
                q_nodes.append(node.right)
                q_vals.append(val + node.right.val)

        return res
