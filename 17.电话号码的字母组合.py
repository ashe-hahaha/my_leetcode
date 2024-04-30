#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def outerjoin(self, a:list, b:list):
        res = []
        if len(a)==0:
            return b
        if len(b)==0:
            return a
        for lettera in a:
            for letterb in b:
                res.append(lettera+letterb)
        return res
    def letterCombinations(self, digits: str) -> List[str]:
        alphabet = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res = []
        alphalist = []

        for digit in digits:
            if len(digits)==1:
                tempstr = alphabet[int(digit)]
                for alpha in tempstr:
                    res.append(alpha)
                return res
            else:
                tempstr = alphabet[int(digit)]
                templist = []
                for alpha in tempstr:
                    templist.append(alpha)
                alphalist.append(templist)

        for i in range(len(alphalist)):
            res = self.outerjoin(res,alphalist[i])
        return res
        
# @lc code=end

