#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(dict, path, result):
            if len(result) == len(nums):
                value = []
                for key in result:
                    value.append(dict[key])
                path.add(tuple(value))
            else:
                for key,value in dict.items():
                    if not(key in result):
                        result.append(key)
                        dfs(dict, path, result)
                        result.pop()

        path = set()
        result = []
        dict = {}
        for i in range(len(nums)):
            dict[i] = nums[i]
        dfs(dict, path, result)
        return list(path)
# @lc code=end

