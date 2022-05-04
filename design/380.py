# 380. O(1) 时间插入、删除和获取随机元素
import random


class RandomizedSet:

    def __init__(self):
        self.book = {}
        self.arr = [0] * 20001
        self.tail = 0

    def insert(self, val: int) -> bool:
        if val in self.book:
            return False
        self.book[val] = self.tail
        self.arr[self.tail] = val
        self.tail += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.book:
            return False
        idx = self.book[val]
        self.book.pop(val)
        if self.tail - 1 != idx:
            self.book[self.arr[self.tail - 1]] = idx
            self.arr[idx], self.arr[self.tail - 1] = self.arr[self.tail - 1], self.arr[idx]
        self.tail -= 1
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, self.tail - 1)]


s = RandomizedSet()
print(s.insert(0))
print(s.getRandom())
print(s.remove(0))
print(s.insert(0))