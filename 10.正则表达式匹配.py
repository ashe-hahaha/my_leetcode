#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        end = '.*'
        if end in p:
            return True
        
        i = 0
        j = 0
        state = 0
        while i<len(s) and j<len(p):
            if i>0:
                if s[i-1] == s[i] and p[j] == '*':
                    state = 1
                    if i+1<len(s):
                        i += 1
                    else:
                        i+=1
                        j+=1
                        break
                    continue
                else:
                    state = 0
                    j += 1
            if p[j] != s[i] and p[j] != '.' and state == 0:
                if j+1<len(p):
                    if p[j+1]=='*':
                        if j+2<len(p):
                            j+=2
                        else:
                            j+=1
                    else:
                        break
                else:
                    break
            else:
                i+=1
                j+=1
        
        if i<len(s) or j<len(p):
            print(i,j)
            return False
        else:
            return True

# @lc code=end

