"""
tag: 数组；数学；模拟
1806. 还原排列的最少操作步数
https://leetcode.cn/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
"""


class Solution0:
    """ 首尾元素恒定不变，其他元素以 pivot 为分界，呈现规律变化 """
    def reinitializePermutation(self, n: int) -> int:
        start = 1  # 选定索引为1的元素进行模拟，用其他元素模拟结果一样
                   # (参照Solution0_1)，但是索引大于1的元素不一定存在
        pivot = n / 2  # 分界点
        cnt, x = 0, start
        while True:
            if x < pivot:
                x *= 2
            else:
                x = (x - pivot) * 2 + 1
            cnt += 1
            if x == start:
                return cnt


class Solution0_1:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1

        start = 2
        pivot = n / 2
        cnt, x = 0, start
        while True:
            if x < pivot:
                x *= 2
            else:
                x = (x - pivot) * 2 + 1  # 等价于 x = x * 2 - (n - 1)
            cnt += 1
            if x == start:
                return cnt


class Solution1:
    """ 官解，Solution0 优化版：两个规律可以合并
    注意 任何整数 % 1 == 0，所以 n == 2 必须单独处理 """
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1

        cnt, x = 1, 2
        while True:
            x = x * 2 % (n - 1)
            cnt += 1
            if x == 1:
                return cnt
