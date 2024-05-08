#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickPow(x,n):
            if n == 0:
                return 1
            y = quickPow(x,n//2)
            if n%2 == 0:
                return y*y
            else:
                return y*y*x
        if n>=0:
            res = quickPow(x,n)
        else:
            res = 1/quickPow(x,-n)
        return res
# @lc code=end

