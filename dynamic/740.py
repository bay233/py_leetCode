# 740. 删除并获得点数

class Solution:
    # nums: List[int]
    def deleteAndEarn(self, nums) -> int:
        if not nums: return 0
        if len(nums) < 2: return nums[0]
        max_len = max(nums) + 1
        book = [0] * max_len
        for n in nums:
            book[n] += 1
        dp = [0] * max_len
        dp[1] = book[1] * 1
        dp[2] = max(dp[1], book[2] * 2)
        for i in range(3, max_len):
            dp[i] = max(dp[i - 1], dp[i - 2] + book[i] * i)
        return dp[-1]


s = Solution()
print(s.deleteAndEarn(
    [12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91, 85,
     14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13, 60, 57,
     91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1, 90, 63, 55,
     64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]))
print(s.deleteAndEarn([3,1]))
