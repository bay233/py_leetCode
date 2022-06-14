# 467. 环绕字符串中唯一的子字符串


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = [0] * 26
        a = ord('a')
        j = 1
        for i, c in enumerate(p):
            n = ord(c) - a
            if i >= 1 and (n - ord(p[i - 1]) + a) % 26 == 1:
                j += 1
            else:
                j = 1
            dp[n] = max(dp[n], j)
        return sum(dp)


s = Solution()
print(s.findSubstringInWraproundString("zab"))