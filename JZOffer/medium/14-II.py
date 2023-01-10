"""
tag: 数学；动态规划；大数求余
https://leetcode.cn/problems/jian-sheng-zi-ii-lcof/solution/
剑指 Offer 14- II. 剪绳子 II
"""


# 求 (x^a) % p —— 循环求余法
def remainder(x, a, p):
    rem = 1
    for _ in range(a):
        rem = (rem * x) % p
    return rem


# 求 (x^a) % p —— 快速幂求余
def remainder(x, a, p):
    rem = 1
    while a > 0:
        if a % 2:
            rem = (rem * x) % p
        x = x ** 2 % p
        a //= 2
    return rem
