"""
tag: 树；深度优先搜索；广度优先搜索；递归；队列
199. 二叉树的右视图
https://leetcode.cn/problems/binary-tree-right-side-view/
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution1:
    """ BFS 解法 """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node.val)
        return res


class Solution2:
    """ DFS 解法 + 递归 """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append(node.val)
            depth += 1
            dfs(node.right, depth)
            dfs(node.left, depth)
        res = []
        dfs(root, 0)
        return res
