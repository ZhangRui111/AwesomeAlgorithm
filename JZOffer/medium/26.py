"""
tag: 树；二叉树；深度优先搜索；广度优先搜索；递归
剑指 Offer 26. 树的子结构
https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/?favorite=xb9nqhhg
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution0:
    """ 层序遍历嵌套深度遍历
    层序遍历 A，
    遇到 A 节点的 val 等于 B 根节点的 val 的节点再进行深度遍历子树判断 """

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False

        def dfs(node_A, node_B):
            node_A_left, node_A_right = node_A.left, node_A.right
            node_B_left, node_B_right = node_B.left, node_B.right

            if node_B_left and (
                    not node_A_left or node_A_left.val != node_B_left.val) \
                    or node_B_right and (
                    not node_A_right or node_A_right.val != node_B_right.val):
                return False
            else:
                if not node_B_left:
                    flag_left = True
                else:
                    flag_left = dfs(node_A_left, node_B_left)
                if not node_B_right:
                    flag_right = True
                else:
                    flag_right = dfs(node_A_right, node_B_right)
                return flag_left and flag_right

        root_B = B.val
        cur_A = A
        queue = deque([cur_A])
        while queue:
            node = queue.popleft()
            left_node = node.left
            if left_node:
                queue.append(left_node)
            right_node = node.right
            if right_node:
                queue.append(right_node)
            if node.val == root_B:
                if dfs(node, B):
                    return True
        return False


class Solution1:
    """ 代码更简洁 先序遍历 """
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (
                recur(A, B) or self.isSubStructure(A.left, B)
                or self.isSubStructure(A.right, B)
        )
