"""
tag: 树
637. 二叉树的层平均值
https://leetcode.cn/problems/average-of-levels-in-binary-tree/
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_sum / level_size)
        return res


class Solution2:
    """ DFS """
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def dfs(node, depth):
            if not node:
                return
            if len(sums) == depth:
                sums.append(node.val)
                counts.append(1)
            else:
                sums[depth] += node.val
                counts[depth] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        sums, counts = [], []
        dfs(root, 0)
        return [a / b for a, b in zip(sums, counts)]
