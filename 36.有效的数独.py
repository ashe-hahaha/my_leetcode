#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # 读入一个9*9 list，3 rules
        # res = True
        # # 1.每一行只能出现一次
        # for row in board:
        #     flag = [0]*9
        #     for el in row:
        #         if el != '.':
        #             flag[int(el)-1] += 1
        #             if flag[int(el)-1]>1:
        #                 res = False
        
        # # 2.每一列只能出现一次
        # cols = []
        # col = [0]*9
        # for i in range(9):
        #     for j in range(9):
        #         col[j] = board[j][i]
        #     # print(col)
        #     # same as 1.
        #     flag = [0]*9
        #     for el in col:
        #         if el != '.':
        #             flag[int(el)-1] += 1
        #             if flag[int(el)-1]>1:
        #                 res = False
        #     # 这句会产生一个问题，因为赋值是从对象的地址拿，用col append后，每次修改col都会导致已经append上去的col的值同样被修改，所以最后结果全部变为最后一列，我这里的逻辑是每次检查完col是否有重复，不记录，就没问题
        #     # cols.append(col)
        
        # # 3.每一个以粗实线分隔的 3x3 宫内只能出现一次
        # square = []
        # for i in range(0,9,3):
        #     for j in range(0,9,3):
        #         square = []
        #         for x in range(3):
        #             for y in range(3):
        #                 square.append(board[i+x][j+y])
        #         # print(square)
        #         # same as 1.
        #         flag = [0]*9
        #         for el in square:
        #             if el != '.':
        #                 flag[int(el)-1] += 1
        #                 if flag[int(el)-1]>1:
        #                     res = False
                            
        # return res
        
        # 初始化行、列、小九宫格的计数数组
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        subboxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]

        # 遍历数独
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    index = int(num) - 1
                    rows[i][index] += 1
                    columns[j][index] += 1
                    subboxes[i // 3][j // 3][index] += 1

                    # 检查是否有计数超过1
                    if rows[i][index] > 1 or columns[j][index] > 1 or subboxes[i // 3][j // 3][index] > 1:
                        return False
        return True
# @lc code=end

