#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(string,left,right):
                if left>right:
                    return
                if left == 0 and right == 0:
                    res.append(string)
                    return
                if left>0:
                    dfs(string+"(",left-1,right)
                if right>0:
                    dfs(string+")",left,right-1)
        res = []
        string = ''
        dfs(string,n,n)
        return res

# @lc code=end

