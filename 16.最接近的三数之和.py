#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min = 99999
        i=0
        while i < len(nums) and len(nums)>=3 :
            l = i+1
            r = len(nums)-1

            while(l<r):
                if abs(target - (nums[i]+nums[l]+nums[r])) < min:
                    res = [nums[i],nums[l],nums[r]]
                    min = abs(target - (nums[i]+nums[l]+nums[r]))
                if target - (nums[i]+nums[l]+nums[r]) < 0:
                    r-=1
                elif target - (nums[i]+nums[l]+nums[r]) > 0:
                    l+=1
                else:
                    return target
            i+=1
        return res[0]+res[1]+res[2]
# @lc code=end

