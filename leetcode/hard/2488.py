"""
tag: 数组；哈希表；前缀和
2488. 统计中位数为 K 的子数组
https://leetcode.cn/problems/count-subarrays-with-median-k/
"""
from collections import Counter


class Solution0_0:
    """ 思路基本正确（使用了“前缀”，没用上“和”），但超时 """
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # convert/simplify the nums，小于等于数 和 大于数
        n = len(nums)
        lower_flag, larger_flag = 0, n + 1
        nums_ = [lower_flag if i <= k else larger_flag for i in nums]

        # obtain the flag list
        cnt_lower_minus_larger = [0]  # 前缀数组为空，即从第一个元素计数子数组
        for i, v in enumerate(nums_):
            if v == lower_flag:
                cnt_lower_minus_larger.append(cnt_lower_minus_larger[-1] + 1)
            else:
                cnt_lower_minus_larger.append(cnt_lower_minus_larger[-1] - 1)
        idx_k = nums.index(k) + 1

        # 遍历计数
        cnt = 0
        for idx in range(idx_k, n + 1):
            target_v = [cnt_lower_minus_larger[idx],
                        cnt_lower_minus_larger[idx] - 1]
            cnt += cnt_lower_minus_larger[:idx_k].count(target_v[0])
            cnt += cnt_lower_minus_larger[:idx_k].count(target_v[1])
        return cnt


class Solution1:
    def sign(self, num: int) -> int:
        # > 0: 1
        # == 0: 0
        # < 0: -1
        return (num > 0) - (num < 0)

    def countSubarrays(self, nums: List[int], k: int) -> int:
        kIndex = nums.index(k)
        counts = Counter()  # key: 前缀和, val: 前缀和出现次数
        counts[0] = 1  # 空前缀

        # 只需遍历一次
        ans = 0
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += self.sign(num - k)
            if i < kIndex:  # 子数组的左起点
                counts[pre_sum] += 1
            else:  # i >= kIndex  # 根据子数组的右终点选择valid左起点
                prev0 = counts[pre_sum]
                prev1 = counts[pre_sum - 1]
                ans += prev0 + prev1
        return ans
