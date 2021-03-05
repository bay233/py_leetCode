# 72. 编辑距离

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        bookMap = {}

        def dp(i, j):
            if i < 0: return j + 1
            if j < 0: return i + 1

            if bookMap.get((i, j)) != None:
                return bookMap[(i, j)]

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)

            result = min(dp(i - 1, j) + 1, dp(i, j - 1) + 1, dp(i - 1, j - 1) + 1)
            bookMap[(i, j)] = result
            return result

        return dp(len(word1) - 1, len(word2) - 1)

    def minDistance2(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for _ in range(1, n1 + 1):
            dp[_][0] = _
        for _ in range(1, n2 + 1):
            dp[0][_] = _

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1,
                                   dp[i - 1][j] + 1,
                                   dp[i][j - 1] + 1)
        return dp[n1][n2]

s = Solution()
print(s.minDistance2("intention", "execution"))
print(s.minDistance("intention", "execution"))
