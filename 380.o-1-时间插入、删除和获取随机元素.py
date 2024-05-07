#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.list = list()
        self.dict = dict()

    def insert(self, val: int) -> bool:
        if val in self.list:
            return False
        else: 
            # dict的key是唯一的
            self.dict[val] = len(self.dict)
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.list:
            # 找到val所在下标
            index = self.dict[val]
            # list最后一位移到下标处
            self.list[index] = self.list[-1]
            # 更新dict
            self.dict[self.list[-1]] = index
            # 移除最后一位
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

