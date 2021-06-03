# 633. 平方数之和
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(math.sqrt(c))
        while i <= j:
            val = i * i + j * j
            if val > c:
                j -= 1
            elif val < c:
                i += 1
            else:
                return True
        return False


s = Solution()
print(s.judgeSquareSum(4))

