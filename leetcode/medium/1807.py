"""
tag: 数组；哈希表；字符串
1807. 替换字符串中的括号内容
https://leetcode.cn/problems/evaluate-the-bracket-pairs-of-a-string/
"""
import re
from collections import defaultdict


class Solution0_1:
    """ very slow """
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {item[0]: item[1] for item in knowledge}
        pat = re.compile(r"\(.+?\)")  # ? 最短匹配
        src = pat.findall(s)
        for item in src:
            if item[1:-1] in knowledge.keys():
                s = s.replace(item, knowledge[item[1:-1]])
            else:
                s = s.replace(item, '?')
        return s


class Solution0_2:
    """ faster """
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {item[0]: item[1] for item in knowledge}
        res, repl = [], []
        i, len_s = 0, len(s)
        while i < len_s:
            c = s[i]
            if c != '(':
                res.append(c)
                i += 1
            else:
                i += 1
                while i < len_s and s[i] != ')':
                    repl.append(s[i])
                    i += 1
                repl = "".join(repl)
                if repl in knowledge.keys():
                    res.append(knowledge[repl])
                else:
                    res.append('?')
                repl = []
                i += 1
        return "".join(res)


class Solution1:
    """ 官解 """
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        ans, start = [], -1
        for i, c in enumerate(s):
            if c == '(':
                start = i
            elif c == ')':
                ans.append(d.get(s[start + 1: i], '?'))
                start = -1
            elif start < 0:
                ans.append(c)
        return "".join(ans)


class Solution2:
    """ 评论区神解 """
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = defaultdict(lambda: '?', knowledge)
        return s.replace('(', '{').replace(')', '}').format_map(d)
