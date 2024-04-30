#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if nums[l]<nums[mid]:
                #左边有序
                if nums[l]<=target and target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            elif nums[l]>nums[mid]:
                #右边有序
                if nums[mid+1]<=target and target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                #两边都有序
                if nums[l]<=target and target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return -1
# @lc code=end

