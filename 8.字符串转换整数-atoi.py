#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        signal = 0
        l = 0
        if not s:
            return 0
        # step 1
        for i in range(len(s)):
            if s[i] != ' ':
                l = i
                break
        # step 2
        if s[l]=='-':
            signal = -1
            l+=1
        elif s[l]=='+':
            l+=1
        
        l
        res = ''
        while l<len(s) and '0'<=s[l] and s[l]<='9':
            res+=s[l]
            l+=1

        print(res)
        if not res:
            res = 0
        res = int(res)
        if signal==-1:
            res = -res
            res = max(res,-2**31)
        else:
            res = min(res,2**31-1)
        
        return res
            
# @lc code=end

