# 583. 两个字符串的删除操作

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(1, len(word1) + 1):
            dp[0][i] = ord(word1[i - 1])
        for i in range(1, len(word2) + 1):
            dp[i][0] = ord(word2[i - 1])

        print(dp)
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i -1][j -1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(word2[i - 1]), dp[i][j - 1] + ord(word1[j - 1]))
                print(dp)

        return dp[-1][-1]

s = Solution()
print(s.minDistance("sea", "eat"))
