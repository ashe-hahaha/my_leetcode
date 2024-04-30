#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        windowLeft = 0
        windowRight = 0
        windowLen = 0

        if s:
            maxlen = 1
            for i in range(len(s)):
                windowLen = windowRight-windowLeft
                if windowLen == 0:
                    windowRight += 1
                    continue
                else:
                    if s.find(s[i],windowLeft,windowRight) == -1:
                        windowRight += 1
                        windowLen += 1
                        if windowLen>maxlen:
                            maxlen = windowLen
                    else:
                        windowLeft = s.find(s[i],windowLeft,windowRight) + 1
                        windowRight += 1
        else: maxlen = 0
        
        return maxlen
# @lc code=end

