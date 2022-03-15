# 1995. 统计特殊四元组


List = list

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for a1 in range(n):
            for a4 in range(a1 + 3, n):
                a2 = a1 + 1
                t = nums[a4] - nums[a1]
                book = {}
                for i in range(a2, a4):
                    s = t - nums[i]
                    if s in book:
                        ans += book[s]
                    if nums[i] in book:
                        book[nums[i]] += 1
                    else:
                        book[nums[i]] = 1
        return ans


s = Solution()
print(s.countQuadruplets([1,1,1,3,5]))

