# 673. 最长递增子序列的个数

List = list

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp = [1] * nums_len
        dp_num = [1] * nums_len
        max_len = 0
        for i in range(1, nums_len):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp_num[i] = dp_num[j]
                        dp[i] = dp[j] + 1
                    elif dp[i] == dp[j] + 1:
                        dp_num[i] += dp_num[j]
            max_len = max(max_len, dp[i])

        res = 0
        for i in range(nums_len):
            if dp[i] == max_len:
                res += dp_num[i]
        return res if res else 1

s = Solution()
print(s.findNumberOfLIS([1,3,5,4,7]))