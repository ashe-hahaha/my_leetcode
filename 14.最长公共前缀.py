#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = 999
        targetword = ''
        for word in strs:
            if len(word)<shortest:
                targetword = word
                shortest = len(word)
        if shortest == 0:
            return ""
        for i in range(len(targetword)):
            for word in strs:
                if targetword[i] != word[i]:
                    return targetword[0:i]
        return targetword
# @lc code=end