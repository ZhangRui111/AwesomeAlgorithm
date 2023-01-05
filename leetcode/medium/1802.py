"""
tag: 贪心；二分查找
1802. 有界数组中指定下标处的最大值
https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/
"""


class Solution0_0:
    """ 遍历查找：初始化为值为1的平面，之后以 index 为顶点逐渐拉起一个倒三角形
    超时 """
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        cur_sum, cur_index, radius = n, 1, 0
        while cur_sum <= maxSum:
            low, high = max(0, index - radius), min(n - 1, index + radius)
            radius += 1
            cur_index += 1
            cur_sum += (high - low + 1)
        return cur_index - 1


class Solution0_1:
    """ 优化至通过，但执行用时依然很长 """
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        cur_sum, cur_index, radius = n, 1, 0
        while cur_sum <= maxSum:
            low, high = max(0, index - radius), min(n - 1, index + radius)
            if index - radius < 0 and index + radius > n - 1:
                cur_index += (maxSum - cur_sum) // n
                return cur_index
            radius += 1
            cur_index += 1
            cur_sum += (high - low + 1)
        return cur_index - 1


class Solution1:
    """ 贪心 + 二分查找 """
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = left + (right + 1 - left) // 2
            if self.valid(mid, n, index, maxSum):
                left = mid
            else:
                right = mid - 1
        return left

    def valid(self, mid: int, n: int, index: int, maxSum: int) -> bool:
        """ verify the validation when nums[index] = mid """
        left = index
        right = n - 1 - index
        return mid + self.cal(mid, left) + self.cal(mid, right) <= maxSum

    def cal(self, big: int, length: int) -> int:
        if length < big - 1:  # 梯形 (不包括 big)
            small = big - length
            return ((big - 1 + small) * length) // 2
        else:  # 三角形 + 高为1的底座
            ones = length - (big - 1)
            return (big - 1 + 1) * (big - 1) // 2 + ones


class Solution2:
    """ 假设nums[idx] = m，则整体三角形面积为m平方(类似1234321)，
    减去两角的小三角形就是总面积
    s1的面积为1 + 2 + ... + m-(idx+1)，等差数列
    s2同理，1 + 2 + ... + m-(n-idx)
    二分高度m即可 """
    def maxValue(self, n: int, idx: int, maxSum: int) -> int:
        l, r = -1, maxSum + 1
        maxSum -= n  # 第一层
        while l + 1 < r:
            m = l + r >> 1
            x, y = m - idx - 1, m - n + idx
            s = m ** 2
            s1, s2 = max(0, x) * (x + 1) // 2, max(0, y) * (y + 1) // 2
            if s - s1 - s2 <= maxSum:
                l = m
            else:
                r = m
        return l + 1
