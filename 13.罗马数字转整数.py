#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        def a2n(dict,targetvalue):
            for key,value in dict.items():
                if value == targetvalue:
                    return key
        symDict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',
            4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM',}
        
        total = 0
        # for i in range(len(s)):
        #     if i+1<len(s):
        #         # 如果左小于右，则两个字母组合
        #         if a2n(symDict,s[i])<a2n(symDict,s[i+1]):
        #             tempnum = a2n(symDict,s[i]+s[i+1])
        #             i+=1
        #         # 左大于等于右，读单独字母
        #         else:
        #             tempnum = a2n(symDict,s[i])
        #     # 最后一个单独字母
        #     else:
        #         tempnum = a2n(symDict,s[i])
        #     print(i,tempnum)
        #     total += tempnum
        i=0
        while i < len(s):
            if i+1<len(s):
                # 如果左小于右，则两个字母组合
                if a2n(symDict,s[i])<a2n(symDict,s[i+1]):
                    tempnum = a2n(symDict,s[i]+s[i+1])
                    i+=2
                # 左大于等于右，读单独字母
                else:
                    tempnum = a2n(symDict,s[i])
                    i+=1
            # 最后一个单独字母
            else:
                tempnum = a2n(symDict,s[i])
                i+=1
            print(i,tempnum)
            total += tempnum

        return total

# @lc code=end