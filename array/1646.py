# 1646. 获取生成数组中的最大值

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        book = [0] * (n + 1)
        book[1] = 1
        res_max = 1
        for i in range(1, n // 2 if not n & 1 else n // 2 + 1):
            book[i * 2] = book[i]
            book[i * 2 + 1] = book[i] + book[i + 1]
            res_max = max(res_max, book[i * 2], book[i * 2 + 1])
        return res_max

s = Solution()
print(s.getMaximumGenerated(2))

