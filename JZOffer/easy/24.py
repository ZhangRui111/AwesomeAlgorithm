"""
tag: 递归；链表
24. 反转链表
https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/?favorite=xb9nqhhg
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution0:
    """ 迭代 """
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head

        cur, cur_nex = head, head.next
        while cur_nex:
            tmp = cur_nex.next
            cur_nex.next = cur
            cur = cur_nex
            cur_nex = tmp
        head.next = None  # 额外的这一步十分重要，不然在遍历链表的时候会死循环
        return cur


class Solution1:
    """ 迭代优化 """
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


class Solution1_1:
    """ 利用 Python 语言的平行赋值语法，可以进一步简化代码 (但可读性下降)
    平行赋值语法：右侧暂存为数组，左边从左到右依次赋值 """
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


class Solution2:
    """ 递归 """
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur:
                return pre  # 终止条件: 仅执行了一次，pre 保存为 res 并一直没变
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre  # 修改节点引用指向
            return res  # 返回反转链表的头节点

        return recur(head, None)  # 调用递归并返回
