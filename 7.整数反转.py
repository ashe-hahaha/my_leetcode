#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        origin_str = str(x)
        reversed_str = ''
        flag = 0
        pos = 0

        if origin_str[0] == '-':
            pos = 1
            flag = 1
        i = len(origin_str)-1
        while(i>=pos):
            reversed_str += origin_str[i]
            i-=1
        res = int(reversed_str)
        if flag==1:
            res = 0-res
        
        if res>pow(2,31)-1 or res<-pow(2,31):
            return 0
        
        return res
# @lc code=end

