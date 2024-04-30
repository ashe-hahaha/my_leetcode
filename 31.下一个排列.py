#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 需要交换的位置在前面小于后面的地方
        # 交换对象为位置在需要交换的位置之后，且只比交换位置元素大的数组元素
        l = len(nums)
        exchange_index = -1
        target_index = -1
        for i in range(l-2,-1,-1):
            if nums[i]<nums[i+1]:
                exchange_index = i
                break
        if exchange_index != -1:
            for i in range(exchange_index+1,l):
                flag = 0
                if nums[i]>nums[exchange_index]:
                    flag = 1
                for el in nums[exchange_index+1:]:
                    if nums[i]>el and el>nums[exchange_index]:
                        flag = 0
                        break
                if flag == 1:
                    target_index = i
                    break
            
            temp = nums[exchange_index]
            nums[exchange_index] = nums[target_index]
            nums[target_index] = temp

        print(exchange_index)
        print(target_index)

        # 将exchange_index之后的元素按升序排列
        nums[exchange_index+1:] = sorted(nums[exchange_index+1:])

# @lc code=end

