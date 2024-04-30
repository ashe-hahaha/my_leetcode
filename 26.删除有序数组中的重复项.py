#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i < len(nums):
            if i>0:
                if nums[i]==nums[i-1]:
                    del nums[i]
                else:
                    i+=1
            else:
                i+=1
        return len(nums)
# @lc code=end

