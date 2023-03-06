"""
tag: 二叉树；深度优先搜索；广度优先搜索；递归
112. 路径总和
https://leetcode.cn/problems/path-sum/
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution0_error:
    """
    输入：
        [1,2]
        1
    输出：
        true
    预期结果：
        false
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, cur_sum):
            cur_sum += node.val
            if cur_sum == targetSum:
                return True
            if cur_sum < targetSum:
                if node.left:
                    if dfs(node.left, cur_sum):
                        return True
                if node.right:
                    if dfs(node.right, cur_sum):
                        return True
            return False

        return dfs(root, 0)


class Solution0:
    """ 深度优先搜索 """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, cur_sum):
            cur_sum += node.val

            if not node.left and not node.right:
                if cur_sum == targetSum:
                    return True
                else:
                    return False

            if node.left:
                if dfs(node.left, cur_sum):
                    return True
            if node.right:
                if dfs(node.right, cur_sum):
                    return True
            return False

        return dfs(root, 0)


class Solution1:
    """ 宽度优先搜索 """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        q_nodes = deque([root])
        q_vals = deque([root.val])
        while q_nodes:
            node = q_nodes.popleft()
            tmp = q_vals.popleft()
            if not node.left and not node.right:
                if tmp == targetSum:
                    return True
            if node.left:
                q_nodes.append(node.left)
                q_vals.append(tmp + node.left.val)
            if node.right:
                q_nodes.append(node.right)
                q_vals.append(tmp + node.right.val)
        return False


class Solution2:
    """ 递归
    观察要求我们完成的函数，我们可以归纳出它的功能：询问是否存在从当前节点 root
    到叶子节点的路径，满足其路径和为 sum。

    假定从根节点到当前节点的值之和为 val，我们可以将这个大问题转化为一个小问题：
    是否存在从当前节点的子节点到叶子的路径，满足其路径和为 sum - val。 """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return self.hasPathSum(root.left,
                               targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val)
