"""
tag: 树；深度优先搜索；广度优先搜索
515. 在每个树行中找最大值
https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution1:
    """ BFS """
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            level_res = []
            for _ in range(level_size):
                node = queue.popleft()
                level_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max(level_res))
        return res


class Solution2:
    """ DFS """
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append(node.val)
            else:
                res[depth] = max(res[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        res = []
        dfs(root, 0)
        return res
