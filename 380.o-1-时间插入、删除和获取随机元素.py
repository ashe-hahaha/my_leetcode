#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.set1 = []

    def insert(self, val: int) -> bool:
        if val in self.set1:
            return False
        else: 
            self.set1.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.set1:
            del(self.set1[self.set1.index(val)])
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.set1)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

