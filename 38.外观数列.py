#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        array = [[1],[1,1]]

        for i in range(1,n-1):
            index = 1
            temp_list = []
            while index<len(array[i]):
                temp_count = 1
                num = array[i][index-1]
                while index<len(array[i]) and array[i][index] == array[i][index-1]:
                    index+=1
                    temp_count+=1
                count = temp_count
                temp_list.append(count)
                temp_list.append(num)
                if index==len(array[i])-1:
                    temp_list.append(1)
                    temp_list.append(array[i][index])
                    break
                else: 
                    index+=1
            array.append(temp_list)
            print(array)

        res = ''
        for el in array[n-1]:
            res+=str(el)
        return res
# @lc code=end

