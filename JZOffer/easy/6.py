"""
tag: 栈；递归；链表
剑指 Offer 06. 从尾到头打印链表
https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/?favorite=xb9nqhhg
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution0:
    """ 辅助栈 """
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        node = head
        while node:
            res.append(node.val)
            node = node.next
        return res[::-1]


class Solution1:
    """ 递归 """
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []
