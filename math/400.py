# 400. 第 N 位数字

import math

class Solution:
    def findNthDigit(self, n: int) -> int:
        len = 1
        while len * 9 * math.pow(10, len - 1) < n:
            n -= len * 9 * math.pow(10, len - 1)
            len += 1
        s = math.pow(10, len - 1)
        x = n // len - 1 + s
        n -= (x - s + 1) * len
        return int(x % 10) if not n else int((x + 1) // math.pow(10, len - n) % 10)
