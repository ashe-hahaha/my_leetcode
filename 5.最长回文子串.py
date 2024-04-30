#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenth = 1
        maxlen = 0
        left = 0
        right = 0
        res_left = 0
        res_right = 0
        for i in range(len(s)):
            lenth = 1
            j = i
            left = i
            right = i
            while j+1<len(s):
                if s[j] == s[j+1]:
                    lenth += 1
                    right += 1
                    if lenth>maxlen:
                        maxlen = lenth
                        res_right = right
                        res_left = left
                    j += 1
                else:
                    break
            while(left-1>=0 and right+1<len(s)):
                # 判断左右是否相同
                left -= 1
                right += 1
                if s[left] == s[right]:
                    lenth += 2
                    if lenth>maxlen:
                        maxlen = lenth
                        res_left = left
                        res_right = right
                else:
                    # 不相同则中断，从下一个字母继续开始找
                    break
        # 左闭右开
        return str(s[res_left:res_right+1])

# @lc code=end