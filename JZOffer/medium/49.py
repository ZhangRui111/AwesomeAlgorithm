"""
tag: 哈希表；数学；动态规划；堆 (优先队列)
剑指 Offer 49. 丑数
https://leetcode.cn/problems/chou-shu-lcof/?favorite=xb9nqhhg
"""
import heapq


class Solution1:
    """ 最小堆解法 """
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            cur = heapq.heappop(heap)
            for factor in factors:
                nxt = cur * factor
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

                # # 赋值表达式/海象运算符 Python >= 3.8
                # if (nxt := cur * factor) not in seen:
                #     seen.add(nxt)
                #     heapq.heappush(heap, nxt)

        return heapq.heappop(heap)


class Solution2:
    """ 动态规划解法 """
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]
