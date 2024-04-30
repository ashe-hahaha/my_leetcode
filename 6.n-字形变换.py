#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        lenth = len(s)
        mode = 0
        x,y = 0,0
        if numRows==1:
            numCols = lenth
            return s
        else:
            groupsize = numRows+numRows-2
            a = lenth//groupsize
            b = lenth%groupsize
            if b//numRows>=1:
                numCols = int((numRows-1)*a + b%numRows + 1)
            else:
                numCols = int((numRows-1)*a + 1)

        mat = [[1 for i in range(numCols)]for j in range(numRows)]
        mat[0][0] = s[0]
        i += 1
        while(i<lenth):
            # 把字母填入mat
            if mode == 0:
                if y+1<numRows:
                    y = y+1
                    mat[y][x] = s[i]
                else:
                    mode = 1
                    y = y-1
                    x = x+1
                    mat[y][x] = s[i]
            elif mode == 1:
                if y-1>=0:
                    y = y-1
                    x = x+1
                    mat[y][x] = s[i]
                else:
                    mode = 0
                    y = y+1
                    mat[y][x] = s[i]
            i += 1
        
        result = ""
        for i in range(numRows):
            for j in range(numCols):
                if mat[i][j]!=1:
                    result += mat[i][j]
        
        return result

# @lc code=end