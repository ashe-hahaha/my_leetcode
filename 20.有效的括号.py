#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def push(self,stack:list,num:int):
        stack.append(num)
        return stack
    def pop(self,stack):
        temp = stack[-1]
        del stack[-1]
        return temp
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol == '(':
                self.push(stack,1)
            if symbol == ')':
                if len(stack) == 0 or self.pop(stack) != 1:
                    return False
            if symbol == '[':
                self.push(stack,2)
            if symbol == ']':
                if len(stack) == 0 or self.pop(stack) != 2:
                    return False
            if symbol == '{':
                self.push(stack,3)
            if symbol == '}':
                if len(stack) == 0 or self.pop(stack) != 3:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

# @lc code=end

