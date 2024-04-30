#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = 0
        sum = 0
        xcopy = x
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        
        while x>0:
            num = x % 10
            sum += num*(10**(len(str(xcopy))-1-c))
            c += 1
            x = x//10
        if xcopy != sum:
            return False
        else:
            return True

# @lc code=end

