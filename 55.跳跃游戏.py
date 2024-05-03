#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
    #     def judge_reach(nums, target_index):
    #         if target_index==0:
    #             return True
    #         else:
    #             for i in range(target_index-1, -1, -1):
    #                 if target_index-i <= nums[i]:
    #                     if judge_reach(nums,i):
    #                         return True
    #         if target_index>0:
    #             return False
    #     return judge_reach(nums, len(nums)-1)

    # greedy
    
        # def max_jump(nums, target_index):
        #     max = 0
        #     i = target_index+1
        #     while i<len(nums) and i<=target_index+nums[target_index]:
        #         max_len = i-target_index+max_jump(nums, i)
        #         if max_len>max:
        #             max = max_len
        #         if max_len>len(nums)-1:
        #             break
        #         i+=1
        #     return max

        # max_len = max_jump(nums,0)
        # if max_len>=len(nums)-1:
        #     return True
        # else:
        #     return False

        keke = 1
        for i in range(len(nums)):
            keke -= 1
            if keke<0:
                return False
            if i+keke>=len(nums)-1:
                return True
            if nums[i]>keke:
                keke = nums[i]
            print(i)
            
            
# @lc code=end

