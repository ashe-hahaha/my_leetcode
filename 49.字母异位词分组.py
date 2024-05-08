#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sorted_word = ''.join(sorted(list(word)))
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word] = [word]
        return list(groups.values())
                
# @lc code=end

