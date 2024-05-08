#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i>j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[i])-j-1]
                matrix[i][len(matrix[i])-j-1] = temp

# @lc code=end

