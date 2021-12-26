# 384. 打乱数组

import random

List = list


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.org = nums.copy()
        self.n = len(self.org)

    def reset(self) -> List[int]:
        self.nums = self.org.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        l, r = 0, self.n - 1
        for i in range(self.n):
            idx = random.randint(l, r)
            self.nums[i], self.nums[idx] = self.nums[idx], self.nums[i]
        return self.nums


s = Solution([1, 2, 3])
print(s.shuffle())
print(s.reset())
print(s.shuffle())
