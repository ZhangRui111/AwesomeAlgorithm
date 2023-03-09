"""
tag: 哈希表；链表
剑指 Offer 35. 复杂链表的复制
https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/?favorite=xb9nqhhg
"""
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution1:
    """ 哈希表 + 两次遍历 """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 初始化哈希表
        dic = dict()
        # 第一次遍历：创建新节点并建立新旧节点的映射关系
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        # 第二次遍历：构建 next 和 random 指针；注意节点为空的情况
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next

        return dic[head]


class Solution2:
    """ 链表拼接 + 拆分 """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. 拼接链表
        cur = head
        while cur:
            nxt = cur.next
            cur.next = Node(cur.val, next=nxt)
            cur = nxt
        # 2. 构建 random 指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3-(a). 拆分链表 & 构建 next 指针
        res = head.next
        pre, cur = head, res
        while pre:
            pre.next = pre.next.next  # 右侧的 pre.next 必不为空
            pre = pre.next
            if cur.next:  # cur.next 可能为空
                cur.next = cur.next.next
            cur = cur.next
        return res
        # # 3-(b). 拆分链表 & 构建 next 指针
        # res = head.next
        # pre, cur = head, res
        # while cur.next:
        #     pre.next = pre.next.next
        #     pre = pre.next
        #     cur.next = cur.next.next
        #     cur = cur.next
        # pre.next = None  # 单独处理原链表尾节点
        # return res
