#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, result):
            if len(result) == len(nums):
                path.append(result.copy())
            else:
                for i in range(len(nums)):
                    if not (nums[i] in result):
                        result.append(nums[i])
                        dfs(nums, path, result)
                        result.pop()
        
        path = []
        result = []
        dfs(nums, path, result)
        return path
# @lc code=end

