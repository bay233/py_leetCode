# 693. 交替位二进制数

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = n & 1
        while n > 0:
            n = n >> 1
            t = n & 1
            if not (t ^ b):
                return False
            b = t
        return True


s = Solution()
print(s.hasAlternatingBits(5))