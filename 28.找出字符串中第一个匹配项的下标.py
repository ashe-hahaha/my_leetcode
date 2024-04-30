#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        while i+len(needle)-1 < len(haystack):
            if haystack[i:i+len(needle)] == needle[:]:
                return i
            else:
                i+=1
        return -1
# @lc code=end

