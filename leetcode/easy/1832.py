"""
tag: 哈希表，字符串
1832. 判断句子是否为全字母句
https://leetcode.cn/problems/check-if-the-sentence-is-pangram/
"""


class Solution1:
    """ 哈希表 (set) """
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


class Solution2:
    """ 位运算: 位或，移位 """
    def checkIfPangram(self, sentence: str) -> bool:
        mask = 0
        for c in sentence:
            mask |= 1 << (ord(c) - ord('a'))
            # mask = mask | (1 << (ord(c) - ord('a')))  # 等价表达式
        return mask == (1 << 26) - 1
