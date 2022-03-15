# 1332. 删除回文子序列


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]:
                return 2
            l += 1
            r -= 1
        return 1

s = Solution()
print(s.removePalindromeSub("ababa"))