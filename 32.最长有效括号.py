#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lst = 0
        j = 0

        lc = 0
        sum_lc = 0
        # 初始栈底元素
        stack = [-1]
        # stack清空时，表示一个有效括号串
        while j<len(s):
            if s[j]=='(':
                stack.append(j)
            elif s[j]==')':
                # 错误：lc记录当前串的最长有效长度，遇到）时，有效串结束，最长有效串为）位置-上一个（位置
                # '始终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」'
                # 正确：最长有效串为：）位置-stack中pop上一个元素后，栈顶元素的index，这样可以解决如()()，也可以解决()
                if len(stack) != 0:
                    if stack[-1] != -1 and s[stack[-1]] == '(':
                        del stack[-1]
                        l_index = stack[-1]
                        lc = j-l_index
                        if lc>lst:
                            lst = lc
                    else:
                        stack.append(j)
                elif len(stack) == 0:
                    stack.append(j)
            j += 1

        return lst
# @lc code=end

