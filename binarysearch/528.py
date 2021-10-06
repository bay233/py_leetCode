# 528. 按权重随机选择

import random

List = list


class Solution:

    def __init__(self, w: List[int]):
        self.sum_w = [0] * (len(w) + 1)
        for i in range(1, len(w) + 1):
            self.sum_w[i] = self.sum_w[i - 1] + w[i - 1]

    def pickIndex(self) -> int:
        ran = random.randint(1, self.sum_w[-1])
        l, r = 1, len(self.sum_w) - 1
        while l <= r:
            mid = l + r >> 1
            if self.sum_w[mid] >= ran:
                r = mid - 1
            if self.sum_w[mid] < ran:
                l = mid + 1
        return r

s = Solution([1,3])
for i in range(20):
    print(s.pickIndex())

