#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            flag = 0
        else:
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        res = ''
        l = 0
        r = 1
        # [l,r)
        remainder = 0
        while l<len(str(dividend)) and r<=len(str(dividend)):
            if remainder == 0:
                temp_dividend_str = str(dividend)[l:r]
            else:
                temp_dividend_str = str(remainder) + str(dividend)[l:r]
            while int(temp_dividend_str)<divisor and r<len(str(dividend)):
                r+=1
                res+='0'
                temp_dividend_str = str(dividend)[l:r]
            temp_dividend = int(temp_dividend_str)
            
            count = 0
            while temp_dividend>=divisor:
                temp_dividend-=divisor
                count+=1
            res+=str(count)
            # 余数等于减完后的暂时被除数
            remainder = temp_dividend

            l = r
            r = l+1

        print(res)
        if flag == 0:
            res = int(res)
        else:
            res = -int(res)

        if res > pow(2,31)-1:
            return pow(2,31)-1
        elif res < -pow(2,31):
            return -pow(2,31)
        else:
            return res
        
# @lc code=end

