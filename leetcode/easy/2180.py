"""
tag: 数学；模拟
2180. 统计各位数字之和为偶数的整数个数
https://leetcode.cn/problems/count-integers-with-even-digit-sum/
"""


class Solution0:
    """ 归纳法：每十个数一个区间，除了第一个区间 [1, 10]外，每个区间有5个数满足条件，
    因此只需要 check 最后几个余数即可 """
    def countEven(self, num: int) -> int:
        a, b = num // 10, num % 10
        cnt = 0
        for n in range(num, num - b - 1, -1):
            if self.check(n):
                cnt += 1
        return cnt + a * 5 - 1

    def check(self, n):
        return sum([int(b) for b in str(n)]) % 2 == 0


class Solution:
    # 这道题只要观察到一点就很简单了：2k 与 2k+1 的各位数字之和的奇偶性不同。于是
    # 可以把自然数按 (2k, 2k+1) 的方式配对，一个区间只有端点可能是单独的点，其他点
    # 一定是成对出现的，只要考虑端点的这个数的各位数字之和的奇偶性即可。即，
    # 当这个数各位和为偶数，返回除以2；各位和为奇数，返回减1再除以2
    def countEven(self, num: int) -> int:
        if self.check(num):
            return num // 2
        else:
            return (num - 1) // 2

    def check(self, n):
        return sum([int(b) for b in str(n)]) % 2 == 0
