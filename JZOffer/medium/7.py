"""
tag: 树；数组；哈希表；分治；二叉树
7. 重建二叉树
https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/?favorite=xb9nqhhg
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution0:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        root_pos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: root_pos + 1],
                                   inorder[:root_pos])
        root.right = self.buildTree(preorder[root_pos + 1:],
                                    inorder[root_pos + 1:])
        return root


class Solution1:
    """ Solution0 中每次在 inorder 中定位根节点时的 index() 操作太耗时 """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(pre_root_idx, in_left_idx, in_right_idx):
            """ 先序遍历的根节点索引，中序遍历的索引左边界，中序遍历的索引右边界 """
            if in_left_idx > in_right_idx:
                return None
            root_val = preorder[pre_root_idx]
            root = TreeNode(root_val)
            i = ht[root_val]
            root.left = recur(pre_root_idx + 1, in_left_idx, i - 1)
            root.right = recur(pre_root_idx + 1 + i - in_left_idx, i + 1,
                               in_right_idx)
            return root

        # 遍历一次，储存中序遍历中所有值的索引
        ht = {}
        for i, val in enumerate(inorder):
            ht[val] = i

        return recur(0, 0, len(inorder) - 1)


