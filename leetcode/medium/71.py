"""
tag: 栈，字符串
71. 简化路径
https://leetcode.cn/problems/simplify-path/
"""
import os
import re


class Solution0:
    def simplifyPath(self, path: str) -> str:
        return os.path.realpath(path)


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p not in ['.', '..', '']:
                stack.append(p)
            elif p == '..' and stack:
                stack.pop()
        # *.join() joins each element of an iterable (such as list, string,
        # and tuple) by a string separator (the string on which the join()
        # method is called)
        return "/" + "/".join(stack)


class Solution_1:
    """ My solution """
    def simplifyPath(self, path: str) -> str:
        # # 这一步并不是必须的，加了这一步也不能完全解决空字符串问题
        # path = re.sub(r"[//]+", "/", path)

        stack = []
        path_chunks = path.split('/')
        for item in path_chunks:
            if item == '.':
                continue
            if item == '..':
                if stack:
                    stack.pop()
                continue
            if item:
                stack.append(item)
        return "/" + "/".join(stack)
