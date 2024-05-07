#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # # 49:1 -> n:n-48
        num11 = 0
        num22 = 0
        single_multi_res = 0
        res = 0
        c = 0
        # for i in range(len(num1)-1,-1,-1):
        #     num11 += (ord(num1[i])-48)*(pow(10,len(num1)-i-1))
        # for i in range(len(num2)-1,-1,-1):
        #     num22 += (ord(num2[i])-48)*(pow(10,len(num2)-i-1))
        # return str(num11*num22)
        for i in range(len(num2)-1,-1,-1):
            single_multi_res = 0
            c = 0
            for j in range(len(num1)-1,-1,-1):
                num11 = int(num2[i])*int(num1[j])+c
                c = num11//10
                single_multi_res += num11 % 10 * pow(10,len(num1)-1-j)
            single_multi_res += c*pow(10,len(num1))
            print(single_multi_res)
            res += single_multi_res * pow(10,len(num2)-1-i)
        return str(res)
# @lc code=end

