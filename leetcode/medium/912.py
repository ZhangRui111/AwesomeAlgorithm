"""
tag: 数组；排序
912. 排序数组
https://leetcode.cn/problems/sort-an-array/
"""
import random
# 排序算法可视化: https://www.cs.usfca.edu/~galles/visualization/Algorithms.html
# LeetCode题解: https://leetcode.cn/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/


class Solution0:
    """ 库函数 """
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums


class Solution1_0:
    """ 快速排序(单向搜索交换 + 随机选取 pivot) """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, low, high):
        if low < high:
            mid = self.randomized_partition(nums, low, high)
            self.quicksort(nums, low, mid - 1)
            self.quicksort(nums, mid + 1, high)

    def randomized_partition(self, nums, low, high):
        pivot_idx = random.randint(low, high)
        self.swap(nums, pivot_idx, high)  # pivot放置到最右边
        pivot = nums[high]
        i = low  # 最左边的一个大于pivot的数可能被swap多次才能到右边合适的位置
        for j in range(low, high):
            if nums[j] < pivot:
                self.swap(nums, i, j)
                i += 1
        self.swap(nums, high, i)
        return i

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


class Solution1_1:
    """ 快速排序(双指针交换 + 随机选取 pivot) """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, low, high):
        if low < high:
            # mid = self.partition(nums, left, right)  # 非随机选择pivot
            mid = self.randomized_partition(nums, low, high)  # 随机选择pivot
            self.quicksort(nums, low, mid - 1)
            self.quicksort(nums, mid + 1, high)

    def partition(self, nums, low, high):
        pivot = nums[low]
        start = low  # low, high 双指针交换
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            while low < high and nums[low] <= pivot:
                low += 1
            if not low < high:
                break
            self.swap(nums, low, high)
        self.swap(nums, start, low)
        return low

    def randomized_partition(self, nums, low, high):
        pivot_idx = random.randint(low, high)  # 随机选择pivot
        self.swap(nums, pivot_idx, low)  # pivot放置到最左边
        return self.partition(nums, low, high)

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


class Solution1_2:
    """
    快速排序(双指针交换 + 随机选取 pivot + special case 处理)

    针对相同元素较多的情况，可以考虑：
    (1) 通过 list --> set --> list 的转化得到 identical元素
    (2) 对所有 identical 元素排序
    (3) 重新插入重复元素，可以在 (1) 之前借助 collections.Counter 保存元素个数
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(set(nums)) > 1:  # 针对全是相同元素的特殊测试用例
            self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, low, high):
        if low < high:
            # mid = self.partition(nums, left, right)  # 非随机选择pivot
            mid = self.randomized_partition(nums, low, high)  # 随机选择pivot
            self.quicksort(nums, low, mid - 1)
            self.quicksort(nums, mid + 1, high)

    def partition(self, nums, low, high):
        pivot = nums[low]
        start = low  # 使用 low, high 双指针双向搜索交换
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            while low < high and nums[low] <= pivot:
                low += 1
            if not low < high:
                break
            self.swap(nums, low, high)
        self.swap(nums, start, low)
        return low

    def randomized_partition(self, nums, low, high):
        pivot_idx = random.randint(low, high)  # 随机选择pivot
        self.swap(nums, pivot_idx, low)  # pivot放置到最左边
        return self.partition(nums, low, high)

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


class Solution2:
    """ 归并排序(递归写法), Merge Sort """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.tmp = []
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums, left, right):
        # 递归终止条件
        if left == right:
            return
        # 分治
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        # 数组的两个子区间本身有序，无需合并
        if nums[mid] <= nums[mid + 1]:
            return
        # 合并两个子区间为一个有序数组
        del self.tmp[:]
        i, j = left, mid + 1
        while i <= mid or j <= right:
            if i > mid or (j <= right and nums[i] > nums[j]):
                self.tmp.append(nums[j])
                j += 1
            else:
                self.tmp.append(nums[i])
                i += 1
        nums[left: right + 1] = self.tmp


class Solution3:
    """ (直接)插入排序, Insertion Sort """
    def sortArray(self, nums: List[int]) -> List[int]:
        n_num = len(nums)
        for i in range(1, n_num):
            temp = nums[i]
            j = i
            while j > 0 and nums[j - 1] > temp:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = temp
        return nums


class Solution4:
    """ 冒泡排序(有提前终止), Bubble Sort """
    def sortArray(self, nums: List[int]) -> List[int]:
        n_nums = len(nums)
        for end in range(n_nums - 1, 0, -1):
            for i in range(end):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums

    def sortArrayWithFlag(self, nums: List[int]) -> List[int]:
        n_nums = len(nums)
        for end in range(n_nums - 1, 0, -1):
            sorted_flag = True
            for i in range(end):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    sorted_flag = False
            if sorted_flag:
                break
        return nums


class Solution5:
    """ (简单)选择排序, Selection Sort """
    def sortArray(self, nums: List[int]) -> List[int]:
        n_num = len(nums)
        for i in range(n_num):
            min_index = i
            for j in range(i + 1, n_num):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums


class Solution6:
    """
    堆排序(下沉建堆)
    https://leetcode.cn/problems/sort-an-array/solution/pai-xu-shu-zu-by-leetcode-solution/
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        array = [0] + nums  # 从索引1开始存储, 节点i的两个子节点索引为2i和2i+1
        n_num = len(nums)
        self.init_heap(array, n_num)
        self.heap_sort(array, nums, n_num)
        return nums

    def init_heap(self, array, n_num):
        # 下沉建堆，从第一个非叶子节点开始
        # [n_num // 2, n_num // 2-1, ..., 1]
        for i in range(n_num // 2, 0, -1):
            self.sink(array, i, n_num)

    def heap_sort(self, array, nums, n_num):
        # 堆排序
        end = n_num
        while end > 1:
            array[1], array[end] = array[end], array[1]
            end -= 1  # 这一步必须在继续下沉之前
            self.sink(array, 1, end)
        nums[:] = array[1:]

    def sink(self, array, index, end):
        while index * 2 <= end:
            # 获取最大子节点
            j = index * 2
            if j + 1 <= end and array[j + 1] > array[j]:
                j += 1
            # 交换操作，父节点下沉，与最大的孩子节点交换
            if array[index] < array[j]:
                array[index], array[j] = array[j], array[index]
                # 继续下沉
                index = j
            else:
                # 提前终止
                break


class Solution7:
    """ 希尔排序(希尔增量) """
    def sortArray(self, nums: List[int]) -> List[int]:
        n_num = len(nums)
        gap = len(nums)  # 增量/序列间隔
        while gap > 1:
            gap = gap // 2  # 可替换为其他增量/序列间隔
            # 子序列分组
            for i in range(gap):
                # 分组后应用直接插入排序, 注意步长不再是1
                for j in range(i + gap, n_num, gap):
                    temp = nums[j]
                    k = j
                    while k > 0 and nums[k - gap] > temp:
                        nums[k] = nums[k - gap]
                        k -= gap
                    nums[k] = temp
        return nums


# ===================================================================
#                              拓展部分
# ===================================================================


class Solution6:
    """ 归并排序 -- 迭代写法 """
    def sortArray(self, nums: List[int]) -> List[int]:
        k = 1
        n_num = len(nums)
        while k < n_num:
            self.mergePass(nums, k, n_num)
            k *= 2
        return nums

    def mergePass(self, nums, k, n_num):
        i = 0
        while i < n_num - 2 * k:
            self.merge(nums, i, i + k - 1, i + 2 * k - 1)
            i += 2 * k
        if i + k < n_num:
            self.merge(nums, i, i + k - 1, n_num - 1)

    def merge(self, nums, left, mid, right):
        tmp = []
        i, j = left, mid + 1
        while i <= mid or j <= right:
            if i > mid or (j <= right and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[left: right + 1] = tmp


class Solution8:
    """ 快速排序 -- 交换，迭代（栈）实现 """
    def sortArray(self, nums: List[int]) -> List[int]:
        stack = list()
        stack.append(len(nums) - 1)
        stack.append(0)
        while stack:
            low = stack.pop()
            high = stack.pop()
            if low < high:
                index = self.partation(nums, low, high)
                stack.append(index - 1)
                stack.append(low)
                stack.append(high)
                stack.append(index + 1)
        return nums

    def partation(self, nums, low, high):
        pivot = nums[low]
        start = low
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            while low < high and nums[low] <= pivot:
                low += 1
            if low >= high:
                break
            self.swap(nums, low, high)
        self.swap(nums, start, low)
        return low

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp


class Solution10:
    """ 快速排序 -- 交换，递归实现 + 三数取中 + 三向切分 """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:
            left, right = self.partation(nums, low, high)
            self.quickSort(nums, low, left-1)
            self.quickSort(nums, right+1, high)

    def partation(self, nums, low, high):
        # 三数取中
        mid = low + (high - low) // 2
        if nums[low] > nums[high]:
            self.swap(nums, low, high)
        if nums[mid] > nums[high]:
            self.swap(nums, mid, high)
        if nums[mid] > nums[mid]:
            self.swap(nums, mid, low)
        # 三向切分
        pivot = nums[low]
        left = low
        right = high
        i = low + 1
        while i <= right:
            if nums[i] > pivot:
                self.swap(nums, i, right)
                right -= 1
            elif nums[i] == pivot:
                i += 1
            else:
                self.swap(nums, i, left)
                left += 1
                i += 1
        return left, right

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp


INSERTION_SORT_MAX_LENGTH = 7


class Solution11:
    """ 快速排序 -- 交换，递归实现 + 三数取中 + 三向切分 + 组合：插入排序 """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:
            # 插入排序
            if high - low <= INSERTION_SORT_MAX_LENGTH:
                self.insertSort(nums, low, high)
                return

            # 三数取中
            mid = low + (high - low) // 2
            if nums[low] > nums[high]:
                self.swap(nums, low, high)
            if nums[mid] > nums[high]:
                self.swap(nums, mid, high)
            if nums[mid] > nums[mid]:
                self.swap(nums, mid, low)
            # 三向切分
            pivot = nums[low]
            left = low
            right = high
            i = low + 1
            while i <= right:
                if nums[i] > pivot:
                    self.swap(nums, i, right)
                    right -= 1
                elif nums[i] == pivot:
                    i += 1
                else:
                    self.swap(nums, i, left)
                    left += 1
                    i += 1
            self.quickSort(nums, low, left - 1)
            self.quickSort(nums, right + 1, high)

    def insertSort(self, nums, low, high):
        for i in range(low + 1, high + 1):
            temp = nums[i]
            j = i - 1
            while j >= 0:
                if nums[j] > temp:
                    nums[j + 1] = nums[j]
                    j -= 1
                else:
                    break
            nums[j + 1] = temp

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


class Solution14:
    """ 计数排序 """
    def sortArray(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        max_num = max(nums)
        min_num = min(nums)

        # 设置 presum 数组长度，然后求出我们的前缀和数组，
        # 这里我们可以把求次数数组和前缀和数组用一个数组处理
        presum = [0] * (max_num - min_num + 1)
        len_presum = len(presum)
        # 次数数组
        for n in nums:
            presum[n - min_num] += 1
        # 前缀和数组
        for i in range(1, len_presum):
            presum[i] = presum[i - 1] + presum[i]

        # 临时数组
        temp = [-1] * len_nums
        # 逆序遍历数组，开始排序,注意偏移量
        for i in reversed(range(len_nums)):
            # 查找 presum 字典，然后将其放到临时数组，注意偏移度
            offset = nums[i] - min_num
            index = presum[offset] - 1
            temp[index] = nums[i]
            # 相应位置减一
            presum[offset] -= 1

        return temp
