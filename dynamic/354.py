# 354. 俄罗斯套娃信封问题

from functools import cmp_to_key


class Solution:

    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        def sortkey(x, y):
            if x[0] == y[0]:
                return y[-1] - x[-1]
            else:
                return x[0] - y[0]

        res = sorted(envelopes, key=cmp_to_key(sortkey))
        data = [r[-1] for r in res]
        return self.lengthOfLIS2(data)

    def lengthOfLIS2(self, nums: list[int]) -> int:
        tail, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tail[m] < num:
                    i = m + 1
                else:
                    j = m
            tail[i] = num
            if j == res: res += 1
        return res

    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]




s = Solution()
print(s.maxEnvelopes([[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]))
print(s.lengthOfLIS2([4,10,4,3,8,9]))
