"""
tag: 二叉树；深度/广度优先搜索
剑指 Offer 28. 对称的二叉树
https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/?favorite=xb9nqhhg
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution0_1:
    """ 迭代/广度优先搜索 (以层为单位判断) """
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        q = deque([root])
        while q:
            level_res = []
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                level_res.append(node.val)
                if node.left:
                    q.append(node.left)
                else:
                    if node.val != 'null':  # 辅助节点用于每层位置对称的判断
                        q.append(TreeNode('null'))
                if node.right:
                    q.append(node.right)
                else:
                    if node.val != 'null':
                        q.append(TreeNode('null'))

            # half_size = (len(level_res) + 1) // 2
            # if level_res[:half_size] != level_res[::-1][:half_size]:
            #     return False
            if level_res != level_res[::-1]:
                return False
        return True


class Solution0_2:
    """ 递归/深度优先搜索 (以节点为单位判断) """
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(left, right):
            if not left and not right:
                return True
            # elif left and not right or not left and right or \
            #         left.val != right.val:
            #     return False
            elif not left or not right or left.val != right.val:  # 更简洁的等价写法
                return False
            else:
                return dfs(left.left, right.right) and dfs(left.right,
                                                           right.left)

        return dfs(root.left, root.right)


class Solution1_1:
    """ 官解：迭代/广度优先搜索 (跟 Solution1_2 一样的思路) """
    # 初始化时我们把根节点入队两次。每次提取两个结点并比较它们的值（队列中每两个连续的
    # 结点应该是相等的，而且它们的子树互为镜像），然后将两个结点的左右子结点按相反的顺
    # 序插入队列中。当队列为空时，或者我们检测到树不对称（即从队列中取出两个不相等的连
    # 续结点）时，该算法结束。
    def isSymmetric(self, root: TreeNode) -> bool:

        def check(left_node, right_node):
            q = deque([left_node, right_node])
            while q:
                left, right = q.popleft(), q.popleft()
                if not left and not right:
                    continue
                if not left or not right or left.val != right.val:
                    return False
                q.append(left.left)
                q.append(right.right)
                q.append(left.right)
                q.append(right.left)

            return True  # 别漏了

        return check(root, root)


class Solution1_2:
    """ 官解：递归/深度优先搜索 """
    def isSymmetric(self, root: TreeNode) -> bool:

        def dfs(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                # 镜像对称的条件
                return left.val == right.val and \
                       dfs(left.left, right.right) and \
                       dfs(left.right, right.left)

        return dfs(root, root)


# # for debug
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)
#
# a = Solution()
# a.isSymmetric(root)
