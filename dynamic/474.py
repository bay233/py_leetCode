# 474. 一和零

class Solution:
    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    def findMaxForm(self, strs, m: int, n: int) -> int:

        def countZeroAndOne(ss):
            zero = 0
            one = 0
            for s in ss:
                if s == "1":
                    one += 1
                else:
                    zero += 1
            return zero, one

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zero, one = countZeroAndOne(s)
            for i in range(m, -1, -1):
                if i >= zero:
                    for j in range(n, -1, -1):
                        if j >= one:
                            dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        return dp[-1][-1]


s = Solution()
print(s.findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))
