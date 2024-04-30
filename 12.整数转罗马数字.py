#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        symDict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',
                   4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM',
                   2:'II',3:'III',6:'VI',7:'VII',8:'VIII',
                   20:'XX',30:'XXX',60:'LX',70:'LXX',80:'LXXX',
                   200:'CC',300:'CCC',600:'DC',700:'DCC',800:'DCCC',
                   2000:'MM',3000:'MMM'}
        numlist = []
        alphalist = []
        c = 0
        res = ''
        while num>0:
            temp = num % 10
            num = num//10
            if temp!= 0:
                numlist.append(temp*(10**c))
            c+=1
        alphalist = numlist.copy()
        for i in range(len(numlist)):
            tempsym = symDict.get(numlist[i],None)
            if tempsym:
                alphalist[i] = tempsym
            else:
                print('missing')
        print(numlist)
        print(alphalist)

        for i in range(len(alphalist)-1,-1,-1):
            res += alphalist[i]
        return res
# @lc code=end

