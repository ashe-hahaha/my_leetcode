#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 优先找左 & 优先找右,且找到后不停,直到找完
        res_l = -1
        res_r = -1

        l,r = 0,len(nums)-1
        # left
        while l<=r:
            mid = (l+r)//2
            if target<=nums[mid]:
                if target == nums[mid]:
                    res_l = mid
                r = mid - 1
            elif target>nums[mid]:
                l = mid + 1

        l,r = 0,len(nums)-1
        # right
        while l<=r:
            mid = (l+r)//2
            if target>=nums[mid]:
                if target == nums[mid]:
                    res_r = mid
                l = mid + 1
            elif target<nums[mid]:
                r = mid - 1
        
        return [res_l,res_r]

# @lc code=end