"""
tag:
剑指 Offer 18. 删除链表的节点
https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/?favorite=xb9nqhhg
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution0:
    """ 双指针 """
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next

        pre = head
        cur = head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
                return head
            else:
                pre = cur
                cur = cur.next
        return head


class Solution1:
    """ 单指针 """
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next

        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return head
            else:
                cur = cur.next
        return head
