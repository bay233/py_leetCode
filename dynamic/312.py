# 312. 戳气球

List = list

class Solution:
    def maxCoins2(self, nums) -> int:
        nums2 = []
        for i in range(len(nums) + 2):
            if i == 0 or i == len(nums) + 1:
                nums2.append(1)
            else:
                nums2.append(nums[i - 1])
        dp = [[0] * len(nums2) for _ in range(len(nums2))]
        for i in range(len(nums2) - 2, -1, -1):
            for j in range(i + 2, len(nums2)):
                max = 0
                for k in range(i + 1, j):
                    tmp = dp[i][k] + dp[k][j] + nums2[i] * nums2[k] * nums2[j]
                    max = tmp if tmp > max else max
                dp[i][j] = max
                print(dp)
        return dp[0][-1]

    def maxCoins(self, nums) -> int:
        book = {}

        def dp(dp_nums):
            if not dp_nums: return 0
            tuple_dp_nums = tuple(dp_nums)
            if tuple_dp_nums in book: return book[tuple_dp_nums]
            max_res = float('-INF')
            for i in range(len(dp_nums)):
                l = dp_nums[i - 1] if i - 1 >= 0 else 1
                r = dp_nums[i + 1] if i + 1 < len(dp_nums) else 1
                num = l * dp_nums[i] * r
                val = dp_nums.pop(i)
                res = dp(dp_nums)
                max_res = max(max_res, res + num)
                dp_nums.insert(i, val)
            book[tuple_dp_nums] = max_res
            return max_res

        return dp(nums)


s = Solution()
print(s.maxCoins2([3,1,5,8]))
