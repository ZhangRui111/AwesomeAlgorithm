"""
tag: 哈希表；字符串；滑动窗口
3. 无重复字符的最长子串
https://leetcode.cn/problems/longest-substring-without-repeating-characters/
"""


class Solution1:
    """ BF """
    def lengthOfLongestSubstring(self, s: str) -> int:
        slen = len(s)
        if slen == 0:
            return 0

        res = 0
        for i in range(slen):
            hashtable = [-1] * 256
            j = 0
            while i + j < slen and hashtable[ord(s[i + j])] < 0:
                hashtable[ord(s[i + j])] = 1
                j += 1
            if res < j:
                res = j

        return res


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        i: head of the target str
        j: tail of the target str
        :param s:
        :return:
        """
        st = {}  # key为某字符，value为字符上次出现的位置 + 1
        i, res = 0, 0
        slen = len(s)
        for j in range(slen):
            if s[j] in st:
                # 新字符 s[j] 之前出现过，考虑是否影响不重复子串的起点
                i = max(st[s[j]], i)
            res = max(res, j - i + 1)
            st[s[j]] = j + 1
        return res

# Solution 2: 动态规划
#   i是截至j，以j为最后一个元素的最长不重复子串的起始位置，即索引范围是[i,j]的子串是
#   以索引j为最后一个元素的最长子串。 当索引从j-1增加到j时，原来的子串[i,j-1]新增了
#   一个元素变为[i,j]，需要判断j是否与[i,j-1]中元素有重复。所以if s[j] in st:是判断
#   s[j]相同元素上次出现的位置，和i孰大孰小。如果i大，说明[i,j-1]中没有与s[j]相同的
#   元素，起始位置仍取i；如果i小，则在[i,j-1]中有了与s[j]相同的元素，所以起始位置变
#   为st[s[j]]+1，即[st[sj]+1,j]。而省略掉的else部分，由于s[j]是第一次出现所以前面
#   必然没有重复的，仍然用i作为起始位置即可。 后面的ans=max(ans,j-i+1)中，括号中前者
#   ans是前j-1个元素最长子串长度，j-i+1是以s[j]结尾的最长子串长度，两者（最长子串要么
#   不包括j，要么包括j）取最大即可更新ans，遍历所有i后得到整个输入的最长子串长度。
