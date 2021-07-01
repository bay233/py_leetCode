# 483. 最小好进制
import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        m = int(n)
        len_max = int(math.log(m) / math.log(2) + 1)
        for len_ in range(len_max, 2, -1):
            k = int(math.pow(m, 1 / (len_ - 1)))
            res = 0
            for i in range(len_): res = res * k + 1
            if res == m: return str(k)
        return str(m - 1)

s = Solution()
print(s.smallestGoodBase("13"))