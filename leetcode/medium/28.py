"""
tag: 双指针；字符串；字符串匹配
28. 找出字符串中第一个匹配项的下标
https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


class Solution0:
    """ str.index() """
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


class Solution1:
    """ BF """
    def strStr(self, haystack: str, needle: str) -> int:
        halen = len(haystack)
        nelen = len(needle)
        if halen < nelen:
            return -1
        if nelen == 0:
            return 0

        for i in range(halen - nelen + 1):
            for j in range(nelen):
                if haystack[i] == needle[j]:
                    i += 1
                else:
                    break
                if j == nelen - 1:
                    return i - nelen

        return -1


class Solution2:
    """
    KMP: https://www.zhihu.com/question/21923021/answer/281346746
    """

    def strStr(self, haystack: str, needle: str) -> int:

        def KMP(s, p):
            """
            s为主串
            p为模式串
            如果t里有p，返回打头下标
            """
            nex = getNext(p)
            i, j = 0, 0  # 分别是s和p的指针
            while i < len(s) and j < len(p):
                if j == -1 or s[i] == p[j]:  # j==-1是由于j=next[j]产生
                    i += 1
                    j += 1
                else:
                    j = nex[j]

            if j == len(p):  # j走到了末尾，说明匹配到了
                return i - j
            else:
                return -1

        def getNext(p):
            """
            p为模式串
            返回next数组，即部分匹配表
            """
            nex = [0] * (len(p) + 1)
            nex[0] = -1
            i = 0
            j = -1
            while i < len(p):
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    nex[i] = j  # 这是最大的不同：记录next[i]
                else:
                    j = nex[j]

            return nex

        return KMP(haystack, needle)


class Solution3:
    """ BM """
    def strStr(self, haystack: str, needle: str) -> int:
        haylen = len(haystack)
        needlen = len(needle)
        return self.bm(haystack, haylen, needle, needlen)

    def badChar(self, b, m):
        """ 存储模式串的哈希表，用来快速求坏字符规则下移动位数 """
        # 初始化
        bc = list()
        for i in range(256):
            bc.append(-1)
        # m代表模式串的长度，如果有两个a, 则后面那个会覆盖前面那个
        for i in range(m):
            ascii_code = ord(b[i])
            bc[ascii_code] = i
        return bc

    def goodSuffix(self, b, m):
        """ 后缀子串和前缀子串匹配表，用来求好后缀规则下的移动位数 """
        # 初始化
        suffix, prefix = list(), list()
        for i in range(m):
            suffix.append(-1)
            prefix.append(False)

        for i in range(m - 1):
            j = i
            k = 0
            while j >= 0 and b[j] == b[m - 1 - k]:
                j -= 1
                k += 1
                suffix[k] = j + 1
            if j == -1:
                prefix[k] = True
        return suffix, prefix

    def move(self, j, m, suffix_index, ispre):
        k = m - 1 - j  # 计算好后缀长度，j代表坏字符的下标
        # 如果含有长度为 k 的好后缀，返回移动位数，
        if suffix_index[k] != -1:
            return j - suffix_index[k] + 1
        # 找头部为好后缀子串的最大长度，从长度最大的子串开始
        for r in range(j + 2, m):
            # 如果是头部
            if ispre[m - r] is True:
                return r
        # 如果没有发现好后缀匹配的串，或者头部为好后缀子串，则移动到m位，也就是匹配串的长度
        return m

    def bm(self, a, n, b, m):
        bc = self.badChar(b, m)
        suffix_index, ispre = self.goodSuffix(b, m)
        i = 0  # 第一个匹配字符
        while i <= (n - m):  # 注意结束条件
            j = m - 1
            # 从后往前匹配，匹配失败，找到坏字符
            while j >= 0:
                if a[i + j] != b[j]:
                    break
                j -= 1
            # 模式串遍历完毕，匹配成功
            if j < 0:
                return i

            # 下面为匹配失败时，如何处理
            # 求出坏字符规则下移动的位数，就是我们坏字符下标减去最靠后匹配坏字符的下标
            x = j - bc[ord(a[i + j])]
            # 好后缀情况，求出好后缀情况下的移动位数,如果不含有好后缀的话，则按照坏字符来
            y = 0
            if y < m - 1 and m - 1 - j > 0:
                y = self.move(j, m, suffix_index, ispre)
            # 移动：综合两规则取最大值
            i = i + max(x, y)

        return -1


if __name__ == '__main__':
    a = Solution2()
    print(a.strStr("adadbfababababcade", "abababca"))
