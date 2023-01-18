"""
tag: 递归；链表；数学
2. 两数相加
https://leetcode.cn/problems/add-two-numbers/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution0_1:
    """ Shortcut 新建链表 """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(head):
            res = []
            cur = head
            while cur:
                res.append(str(cur.val))
                cur = cur.next
            return int("".join(res[::-1]))

        n = traverse(l1) + traverse(l2)
        vals = str(n)[::-1]
        pre_head = ListNode()
        cur = pre_head
        for c in vals:
            cur.next = ListNode(int(c))
            cur = cur.next
        return pre_head.next


class Solution0_2:
    """ 进位解法 + 原地修改 """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        pre_cur1, pre_cur2 = l1, l2
        ret = 0  # 进位
        return_l1 = True
        while cur1 or cur2:
            if cur1 and cur2:
                v1, v2 = cur1.val, cur2.val
                s = v1 + v2 + ret
                v, ret = s % 10, s // 10
                cur1.val, cur2.val = v, v
                pre_cur1, pre_cur2 = cur1, cur2
                cur1, cur2 = cur1.next, cur2.next
            else:
                if not cur1:
                    return_l1 = False
                    v2 = cur2.val
                    s = v2 + ret
                    v, ret = s % 10, s // 10
                    cur2.val = v
                    pre_cur2 = cur2
                    cur2 = cur2.next
                else:
                    v1 = cur1.val
                    s = v1 + ret
                    v, ret = s % 10, s // 10
                    cur1.val = v
                    pre_cur1 = cur1
                    cur1 = cur1.next

        if return_l1:
            if ret > 0:
                pre_cur1.next = ListNode(1)
            return l1
        else:
            if ret > 0:
                pre_cur2.next = ListNode(1)
            return l2


class Solution0_3:
    """ 进位解法 + 新建链表 """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode()
        cur = pre_head

        cur1, cur2 = l1, l2
        ret = 0  # 进位
        while cur1 or cur2:
            v1, cur1 = (cur1.val, cur1.next) if cur1 else (0, None)
            v2, cur2 = (cur2.val, cur2.next) if cur2 else (0, None)
            s = v1 + v2 + ret
            v, ret = s % 10, s // 10
            cur.next = ListNode(v)
            cur = cur.next

        if ret > 0:
            cur.next = ListNode(1)
        return pre_head.next
