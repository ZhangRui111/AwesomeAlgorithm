"""
tag: 链表；双指针
剑指 Offer 22. 链表中倒数第k个节点
https://drive.mindmup.com/map/1Ai_K_IePWfAhWmpo-k1ftur4QqHtzmR3
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution0:
    """ 数组辅助存储 """
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return

        res = []
        node = head
        while node:
            res.append(node)
            node = node.next
        return res[-k]


class Solution1:
    """ 双指针解法 """
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return

        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter
