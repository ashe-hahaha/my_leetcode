#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l = -1
        r = -1
        s = -1
        res = 0
        '''
        高度下降时，前一位置为左柱子。此时右边可能存在更高的柱子
        若存在，取更高为右柱子，计算seg
        若不存在，取右边最高为右柱子，计算seg
        
        从这个右柱子开始，继续寻找左柱子
        '''
        flag = 0
        i = 1
        max_r = 0
        max_r_index = -1
        while i < len(height):
            # flag = 0, 找l
            # 下降时的前一位置为l
            if flag==0:
                if height[i]>=height[i-1]:
                    i+=1
                    continue
                else:
                    l = i-1
                    flag = 1
                    max_r = 0
                    max_r_index = -1
                    # print("l:", l)
            
            # flag = 1, 找r
            if flag == 1:
                # 若存在，第一次出现大于等于heightl的i为r
                if height[i]>=height[l]:
                    r = i
                    # print("r:", r)
                    inside = 0
                    for j in range(l+1,r):
                        inside+=height[j]
                    s = (r-l-1)*height[l] - inside
                    res+=s
                    flag = 0
                    # print("s:", s)

                # 若不是更高，更新右边最高柱子index
                elif height[i]>max_r:
                    max_r = height[i]
                    max_r_index = i
                               
            i+=1
            # 如果已经到底且还没找到（flag==1）,取右边最高为右柱子
            if flag==1 and i==len(height):
                if max_r_index>0:
                    r = max_r_index
                    inside = 0
                    for j in range(l+1,r):
                        inside+=height[j]
                    s = (r-l-1)*height[r] - inside
                    # print("s:", s)
                    res+=s
                    flag = 0
                    # 从右柱子的下一个位置开始下一次循环
                    i = r+1
        return res
        
 
         

# @lc code=end

