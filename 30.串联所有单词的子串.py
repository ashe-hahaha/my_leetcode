#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        # s[i,j)
        # var.index('str')
        # del l1[l1.index('foo')]
        res = []
        s1 = ''
        flag = 1
        if l == 1:
            for y in range(len(words)):
                s1 += words[y]
                if y>0 and s1[y]!=s1[y-1]:
                    flag = 0
            if s1 in s and flag==1:
                for i in range(len(s)-len(s1)+1):
                    res.append(i)
                return res
        for x in range(0, len(s)):
            i = x
            j = x + l
            l1 = words.copy()
            # print(x)
            while j<=len(s):
                test_target = s[i:j]
                # print(l1)
                if test_target in l1:
                    del l1[l1.index(test_target)]
                    if len(l1) == 0:
                        res.append(x)
                    i += l
                    j += l
                else:
                    break
        return res
# @lc code=end

