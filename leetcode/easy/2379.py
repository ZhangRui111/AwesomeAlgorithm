"""
tag: 字符串；滑动窗口
2379. 得到 K 个黑块的最少涂色次数
https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
"""


class Solution0_1:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = k
        for i in range(0, len(blocks) - k + 1):
            res = min(res, blocks[i:i + k].count('W'))
        return res


class Solution0_2_Error:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = blocks[:k].count('W')
        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1] != blocks[i + k - 1]:
                if blocks[i - 1] == 'W':
                    res -= 1
                    if res == 0:
                        break
                else:
                    res += 1
        return res


class Solution0_2:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt = blocks[:k].count('W')
        res = cnt
        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1] != blocks[i + k - 1]:
                if blocks[i - 1] == 'W':
                    cnt -= 1
                    res = min(res, cnt)
                    if cnt == 0:
                        return 0
                else:
                    cnt += 1
        return res
