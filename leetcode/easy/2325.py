"""
tag: 哈希表；字符串
2325. 解密消息
https://leetcode.cn/problems/decode-the-message/
"""


class Solution0:
    def decodeMessage(self, key: str, message: str) -> str:
        seen = set()
        key_ = []
        for c in key:
            if c not in seen and c != ' ':
                key_.append(c)
                seen.add(c)

        key_map = dict(zip(key_, (chr(ord('a') + i) for i in range(26))))
        key_map[' '] = ' '
        decoded_message = "".join(map(lambda k: key_map[k], message))
        return decoded_message


class Solution1:
    """ 官解 """
    def decodeMessage(self, key: str, message: str) -> str:
        cur = "a"
        rules = dict()

        for c in key:
            if c != " " and c not in rules:
                rules[c] = cur
                cur = chr(ord(cur) + 1)

        ans = "".join(rules.get(c, " ") for c in message)
        return ans
