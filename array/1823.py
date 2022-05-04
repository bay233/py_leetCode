# 1823. 找出游戏的获胜者


List =list

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [_ + 1 for _ in range(n)]
        i = 0
        while n > 1:
            idx = (i + k - 1) % n
            arr.pop(idx)
            n -= 1
            i = idx % n
        return arr[0]

s = Solution()
print(s.findTheWinner(n = 6, k = 5))