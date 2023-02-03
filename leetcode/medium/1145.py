"""
tag: 二叉树；广度/深度优先搜索
1145. 二叉树着色游戏
https://leetcode.cn/problems/binary-tree-coloring-game/
"""
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution0_1:
    """ 广度优先搜索 """
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int,
                             x: int) -> bool:
        if n == 1:  # 二叉树只有一个节点
            return False

        # 首先遍历二叉树找到 x 节点
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == x:
                node_x = node
                break
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        # x 位于叶子结点时，y 取 x 的父节点必胜
        if not node_x.left and not node_x.right:
            return True

        # x 不是叶子结点，则计数 x 左子树，右子树，以及父节点连接部分的节点个数
        if not node_x.left:
            cnt_left = 0
        else:
            q_left, cnt_left = deque([node_x.left]), 0
            while q_left:
                node = q_left.popleft()
                cnt_left += 1
                if node.left:
                    q_left.append(node.left)
                if node.right:
                    q_left.append(node.right)
        if not node_x.right:
            cnt_right = 0
        else:
            q_right, cnt_right = deque([node_x.right]), 0
            while q_right:
                node = q_right.popleft()
                cnt_right += 1
                if node.left:
                    q_right.append(node.left)
                if node.right:
                    q_right.append(node.right)

        three_parts = (cnt_left, cnt_right, n - 1 - (cnt_left + cnt_right))
        if max(three_parts) > n // 2:
            return True
        else:
            return False


class Solution0_2:
    """ 深度优先搜索 """
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int,
                             x: int) -> bool:
        if n == 1:  # 二叉树只有一个节点
            return False

        def dfs(node):
            if not node:
                return 0
            if node.val == x:
                nonlocal node_x
                node_x = node
            return 1 + dfs(node.left) + dfs(node.right)

        node_x = None
        dfs(root)

        # x 位于叶子结点时，y 取 x 的父节点必胜
        if not node_x.left and not node_x.right:
            return True

        # x 不是叶子结点
        cnt_left = dfs(node_x.left)
        if cnt_left > n // 2:
            return True
        cnt_right = dfs(node_x.right)
        if cnt_right > n // 2:
            return True
        if n - 1 - (cnt_left + cnt_right) > n // 2:
            return True
        return False
