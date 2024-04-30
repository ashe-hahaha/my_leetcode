#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def ifnotin(self,reslist,target):
        flag = 1
        for rec in reslist:
            if (target[0] in rec) and (target[1] in rec) and (target[2] in rec) and target!=[0,0,0]:
                return False
            if rec == [0,0,0]:
                flag = 0
        if target == [0,0,0] and flag == 0:
            return False
        return True

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # reslist = []
        # targetSum = 0
        # targetSum2 = 0

        # for i in range(len(nums)):
        #     targetSum = 0 - nums[i]
        #     # 减第一个值，问题变为求两数之和
        #     numscopy = nums.copy()
        #     del numscopy[i]
        #     for j in range(len(numscopy)):
        #         targetSum2 = targetSum - numscopy[j]
        #         # 减第二个值，问题变为查一个数
        #         numscopy2 = numscopy.copy()
        #         del numscopy2[j]
        #         for k in range(len(numscopy2)):
        #             if numscopy2[k] == targetSum2:
        #                 target = [nums[i],numscopy[j],numscopy2[k]]
        #                 if self.ifnotin(reslist,target):
        #                     reslist.append(target)
        #                 else:
        #                     continue
        # return reslist
        nums.sort()
        reslist = []
        i=0
        while i < len(nums) and len(nums)>=3 :
            if nums[i]>0:
                break
            # 如果当前数字与前一个数字相同，则跳过以避免重复结果
            # python 'and' 为短路逻辑
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            l = i+1
            r = len(nums)-1

            while(l<r):
                if nums[l]+nums[r] == 0-nums[i]:
                    reslist.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                while l<r and l-1>i and nums[l] == nums[l-1]:
                    l+=1
                while l<r and r+1<len(nums) and nums[r] == nums[r+1]:
                    r-=1
                if nums[l]+nums[r] < 0-nums[i]:
                    l+=1
                elif nums[l]+nums[r] > 0-nums[i]:
                    r-=1                
            i+=1
            
        return reslist
    
# @lc code=end