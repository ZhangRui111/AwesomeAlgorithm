"""
tag: 动态规划
70. 爬楼梯
https://leetcode.cn/problems/climbing-stairs/
"""


# def climbStairs(n: int) -> int:
#     """ Recursion (time-consuming) """
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return climbStairs(n-1) + climbStairs(n-2)


def climbStairs_0(n: int) -> int:
    """ DP """
    if n <= 2:
        return n

    dp = [0, 1, 2]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[-1]


def climbStairs_1(n: int) -> int:
    """ DP (优化空间版) """
    if n <= 2:
        return n

    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


def main():
    print(climbStairs_1(2))
    print(climbStairs_1(3))


if __name__ == '__main__':
    main()
