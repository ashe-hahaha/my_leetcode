#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pass_gain = gas.copy()
        pass_gain_sum = 0
        # acc是passgainsum的累计和，最大的负数的位置的下一个位置就是开始位置
        acc = gas.copy()
        acc_min = 99999999
        acc_min_index = -1

        res = -1
        for i in range(len(gas)):
            pass_gain[i] = gas[i]-cost[i]
            pass_gain_sum+=pass_gain[i]
        
        
        for i in range(0,len(gas)):
            if i==0:
                acc[i] = pass_gain[i]
            else:
                acc[i] = acc[i-1]+pass_gain[i]
            if acc[i]<=acc_min:
                acc_min = acc[i]
                acc_min_index = i

        # print(pass_gain)
        # print(acc)
        if pass_gain_sum<0:
            res = -1
        else:
            res = (acc_min_index+1)%len(gas)
        
        return res
            
# @lc code=end

