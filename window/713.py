# 713. 乘积小于 K 的子数组


List = list


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        ans = 0
        s = 1
        while r < n:
            s *= nums[r]
            while s >= k and l <= r:
                s //= nums[l]
                l += 1
            r += 1
            ans += r - l
        return ans


s = Solution()
print(s.numSubarrayProductLessThanK(nums=[1,2,3], k=0))
