"""
tag: 数组；动态规划
1664. 生成平衡数组的方案数
https://leetcode.cn/problems/ways-to-make-a-fair-array/
"""


class Solution0:
    """ 数学 + 迭代解法 """
    def waysToMakeFair(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        cnt = 0

        # 奇数偶数索引分别计算累加和
        o, e, accum_nums = 0, 0, []
        for i, n in enumerate(nums):
            if i & 1:
                o += n
                accum_nums.append(o)
            else:
                e += n
                accum_nums.append(e)
        odd_sum, even_sum = (accum_nums[-2], accum_nums[-1]) if len(nums) & 1 \
            else (accum_nums[-1], accum_nums[-2])

        for i in range(len(nums)):
            if i == 0:
                new_odd_sum = even_sum - nums[0]
                new_even_sum = odd_sum
            elif i == 1:
                new_odd_sum = even_sum - nums[0]
                new_even_sum = nums[0] + (odd_sum - nums[1])
            elif i & 1:  # i 是奇数
                new_odd_sum = accum_nums[i - 2] + (even_sum - accum_nums[i - 1])
                new_even_sum = accum_nums[i - 1] + (odd_sum - accum_nums[i])
            else:  # i 是偶数
                new_even_sum = accum_nums[i - 2] + (odd_sum - accum_nums[i - 1])
                new_odd_sum = accum_nums[i - 1] + (even_sum - accum_nums[i])

            if new_odd_sum == new_even_sum:
                cnt += 1

        return cnt


class Solution1:
    """ 动态规划 """
    def waysToMakeFair(self, nums: List[int]) -> int:
        res = 0

        # 初始化
        preOdd = preEven = sufOdd = sufEven = 0
        for i, num in enumerate(nums):
            if i & 1:
                sufOdd += num
            else:
                sufEven += num

        for i, num in enumerate(nums):
            # 通项公式
            if i & 1:
                sufOdd -= num
            else:
                sufEven -= num

            # 平衡数组判断
            if preOdd + sufEven == preEven + sufOdd:
                res += 1

            # 通项公式
            if i & 1:
                preOdd += num
            else:
                preEven += num
        return res
