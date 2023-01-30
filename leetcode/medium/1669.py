"""
tag: 链表
1669. 合并两个链表
https://leetcode.cn/problems/merge-in-between-linked-lists/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution0:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur1 = pre1 = list1
        cur2 = pre2 = list2
        cnt = 0
        while cnt < a:
            pre1 = cur1
            cur1 = cur1.next
            cnt += 1
        pre1.next = list2
        while cnt <= b:
            pre1 = cur1
            cur1 = cur1.next
            cnt += 1
        while cur2:
            pre2 = cur2
            cur2 = cur2.next
        pre2.next = cur1
        return list1


class Solution1:
    """ 官解 """
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        preA = list1
        for _ in range(a - 1):
            preA = preA.next
        preB = preA
        for _ in range(b - a + 2):
            preB = preB.next
        preA.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = preB
        return list1
