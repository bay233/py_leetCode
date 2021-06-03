# 1035. 不相交的线

class Solution:
    # def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


s = Solution()
nums1 = [1, 14, 1, 4, 3, 6, 10, 14, 6, 18, 15, 6, 6, 20, 1, 7, 5, 3, 11, 2, 10, 7, 18, 11, 4, 6, 17, 12, 14, 10, 11, 20,
         4, 3, 17, 20, 20, 18, 10, 15, 9, 17, 12, 8, 20, 3, 8, 6, 16, 6, 15, 3, 20, 2, 10, 11, 5, 19, 9, 4, 19, 18, 5,
         2, 18, 4, 11, 9, 19, 16, 9, 1, 8, 4, 9, 19, 19, 11, 5, 7, 4, 7, 16, 15, 9, 16, 15, 13, 6, 2, 4, 19, 10, 19, 16,
         19, 20, 2, 10, 13, 10, 1, 6, 16, 11, 8, 6, 4, 1, 12, 10, 2, 16, 20, 11, 6, 12, 12, 3, 7, 13, 16, 9, 14, 14, 6,
         15, 12, 18, 13, 15, 11, 10, 20, 9, 7, 13, 14, 15, 10, 13, 16, 14, 11, 13, 2, 6, 15, 8, 14, 19, 20, 1, 17, 1,
         10, 5, 15, 13, 17, 11, 3, 1, 15, 1, 12, 9, 9, 4, 18, 3, 11, 16, 20, 2, 18, 9, 5, 15, 20, 16, 17, 9, 13, 1, 2,
         4, 13, 19, 15, 3, 13, 11, 10, 9, 18, 8, 5, 15, 4]
nums2 = [12, 11, 9, 5, 17, 15, 13, 4, 20, 12, 17, 4, 10, 15, 2, 10, 19, 1, 18, 18, 15, 20, 13, 4, 18, 4, 17, 19, 18, 10,
         9, 12, 13, 6, 19, 17, 14, 12, 17, 9, 10, 10, 17, 15, 4, 3, 19, 20, 4, 17, 17, 2, 10, 4, 4, 9, 12, 7, 8, 15, 14,
         4, 1, 6, 17, 10, 12, 14, 17, 4, 5, 8, 6, 11, 8, 5, 4, 17, 5, 19, 5, 11, 9, 3, 9, 20, 7, 8, 16, 14, 17, 12, 19,
         11, 4, 7, 17, 13, 9, 8, 8, 11, 13, 2, 19, 4, 1, 3, 11, 18, 20, 14, 9, 6, 11, 16, 11, 18, 3, 13, 8, 18, 10, 14,
         9, 2, 1, 4, 6, 20, 19, 12, 2, 2, 12, 1, 18, 13, 20, 10, 9, 12, 14, 4, 11, 9, 19, 9, 1, 10, 19, 10, 1, 10, 11,
         4, 4, 4, 14, 10, 5, 19, 3, 19, 7, 4, 20, 14, 7, 9, 9, 5, 12, 4, 1, 6, 2, 14, 14, 5, 16, 10, 15, 11, 1, 16, 11,
         12, 16, 16, 18, 7, 20, 1, 1, 13, 17, 4, 1, 8]
print(s.maxUncrossedLines(nums1, nums2))
