#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # print(nums)
        i = 0
        res = []
        while(i<len(nums)) and len(nums)>=4:
            while i>0 and nums[i]==nums[i-1] and i+1<len(nums):
                i+=1
            j = i+1
            while j<len(nums):
                while j>i+1 and nums[j]==nums[j-1] and j+1<len(nums):
                    j+=1
                temptarget = target-nums[i]-nums[j]
                l=j+1
                r=len(nums)-1
                while l<r:
                    # print(nums[i],nums[j],nums[l],nums[r])
                    # print(i,j,l,r)
                    if l>j+1 and nums[l]==nums[l-1]:
                        l+=1
                        continue
                    if nums[l]+nums[r] == temptarget:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                    elif nums[l]+nums[r]<temptarget:
                        l+=1
                    elif nums[l]+nums[r]>temptarget:
                        r-=1
                j+=1
            i+=1
        return res
# @lc code=end

