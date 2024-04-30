#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def find_key_by_value(self, my_dict, value):
        # 遍历字典中的键值对
        for key, val in my_dict.items():
            # 如果找到对应的值，则返回对应的键
            if val == value:
                return key
        # 如果未找到对应的值，则返回 None
        return None
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        count = 0
        for key in nums:
            numdict[count] = key
            count += 1
        print(numdict)
        for num in nums:
            index1 = self.find_key_by_value(numdict,num)
            index2 = -1
            del numdict[index1]
            print(target - num)
            print(self.find_key_by_value(numdict,target-num))
            if target - num in numdict.values():
                if self.find_key_by_value(numdict,target-num) != index1:
                    index2 = self.find_key_by_value(numdict,target-num)
                break
            numdict[index1] = num
        return index1,index2
# @lc code=end

