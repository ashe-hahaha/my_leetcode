#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        mid = 0
        nums3.sort()
        print(nums3)
        if len(nums3)%2 == 0:
            mid = (nums3[len(nums3)//2] + nums3[len(nums3)//2-1])/2
        else:
            mid = nums3[(len(nums3)-1)//2]

        return mid
# @lc code=end

