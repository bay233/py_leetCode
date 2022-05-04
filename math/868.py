# 868. 二进制间距


class Solution:
    def binaryGap(self, n: int) -> int:
        l = 32
        for i in range(32, -1, -1):
            if n >> i:
                l = i
                break
        ans = 0
        for i in range(l - 1, -1, -1):
            if (n >> i) & 1:
                ans = max(ans, l - i)
                l = i
        return ans


s = Solution()
print(s.binaryGap(22))
