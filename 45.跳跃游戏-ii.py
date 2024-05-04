#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        r=1
        next_r = len(nums)-1

        while r>0:
            max_dist = 0
            r = next_r
            for i in range(r-1,-1,-1):
                dist = r-i
                if dist<=nums[i] and dist>max_dist:
                    max_dist = dist
                    next_r = i
            if r!=0:
                count+=1

        return count

# @lc code=end

