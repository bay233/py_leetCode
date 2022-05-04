# 396. 旋转函数


List = list

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * (n * 2 + 10)
        for i in range(1, 2 * n + 1):
            s[i] = s[i - 1] + nums[(i - 1) % n]
        ans = 0
        for i in range(1, n + 1):
            ans += nums[i - 1] * (i - 1)
        cur = ans
        for i in range(n + 1, 2 * n):
            cur += nums[(i - 1) % n] * (n - 1)
            cur -= s[i - 1] - s[i - n]
            ans = max(ans, cur)
        return ans
