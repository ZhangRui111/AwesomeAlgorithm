"""
tag: 树；深度优先搜索；广度优先搜索
116. 填充每个节点的下一个右侧节点指针
https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/
"""


# # Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next


from collections import deque


class Solution2:
    """ # 标记法 """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            if level_size == 1 and queue[0] == '#':
                break
            queue.append('#')
            for i in range(level_size):
                node = queue.popleft()
                if queue and queue[0] != '#':
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            queue.popleft()
        return root


class Solution2:
    """ prev 指针标记法 """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            prev = None
            for i in range(level_size):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


class Solution3:
    """ 递归解法 """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            if not node:
                return

            left = node.left
            right = node.right
            while left:
                left.next = right
                left = left.right
                right = right.left

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root


class Solution4:
    """ 取代队列的链表优化解法 """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        high_level_node = root
        dummy = Node(0)
        pre = dummy
        while high_level_node:
            while high_level_node:
                if high_level_node.left:
                    pre.next = high_level_node.left
                    pre = pre.next
                if high_level_node.right:
                    pre.next = high_level_node.right
                    pre = pre.next
                high_level_node = high_level_node.next
            high_level_node = dummy.next
            dummy.next = None
            pre = dummy
        return root
