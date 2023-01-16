"""
tag: 数组；双指针；字符串
1813. 句子相似性 III
https://drive.mindmup.com/map/1Ai_K_IePWfAhWmpo-k1ftur4QqHtzmR3
"""


class Solution0:
    """ 4指针 + 多处判定，emmm，面向测试编程 """
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        src_sen, dst_sen = (sentence1, sentence2) if len(sentence1) < len(
            sentence2) else (sentence2, sentence1)
        len_src, len_dst = len(src_sen), len(dst_sen)

        # 两边插入
        if src_sen == dst_sen[:len_src] or src_sen == dst_sen[-len_src:]:
            return True

        # 中间插入
        left_src, right_src = 0, len_src - 1
        left_dst, right_dst = 0, len_dst - 1
        while left_dst < len_dst and left_src < len_src and dst_sen[
            left_dst] == src_sen[left_src]:
            left_dst += 1
            left_src += 1
        while right_dst > 0 and right_src > 0 and right_src > left_src - 1 and \
                dst_sen[right_dst] == src_sen[right_src]:
            right_dst -= 1
            right_src -= 1
        if left_src - right_src == 1:
            return True
        else:
            return False


class Solution1:
    """ 官解双指针 """
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        i, j = 0, 0
        while i < len(words1) and i < len(words2) and words1[i] == words2[i]:
            i += 1
        while j < len(words1) - i and j < len(words2) - i and words1[-j - 1] == words2[-j - 1]:
            j += 1
        return i + j == min(len(words1), len(words2))
