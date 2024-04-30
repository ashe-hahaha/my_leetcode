#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        Smax = 0
        i = 0
        j = len(height) - 1
        while(i<j):
            s = min(height[i],height[j])*(j-i)
            if s>Smax:
                Smax = s
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1

        return Smax
# @lc code=end
    
    