# 390. 消除游戏


class Solution:
    def lastRemaining(self, n: int) -> int:
           if n == 1:
               return n
           return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))


s = Solution()
print(s.lastRemaining(n = 9))