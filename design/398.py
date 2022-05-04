# 398. 随机数索引
import random

List = list


class Solution:

    def __init__(self, nums: List[int]):
        self.book = {}
        for i, n in enumerate(nums):
            if n in self.book:
                self.book.get(n).append(i)
            else:
                self.book[n] = [i]

    def pick(self, target: int) -> int:
        arr = self.book.get(target)
        return arr[random.randint(0, len(arr) - 1)]


s = Solution([1, 2, 3, 3, 3])
print(s.pick(3))
print(s.pick(1))
print(s.pick(3))
