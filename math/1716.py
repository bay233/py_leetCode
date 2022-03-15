# 1716. 计算力扣银行的钱

class Solution:
    def totalMoney(self, n: int) -> int:
        d = (n % 7)
        k = n // 7
        ans = k * d + (1 + d) * d // 2
        if k > 0:
            m = k - 1
            ans += 28 * k + 7 * (1 + m) * m // 2
        return ans


s = Solution()
print(s.totalMoney(20))
