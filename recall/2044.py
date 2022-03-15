# 2044. 统计按位或能得到最大值的子集数目


List = list


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        self.max_val = 0
        self.ans = 0

        def dfs(i, v):
            if i == n:
                return
            val = v | nums[i]
            if val == self.max_val:
                self.ans += 1
            if val > self.max_val:
                self.max_val = val
                self.ans = 1
            dfs(i + 1, v)
            dfs(i + 1, val)

        dfs(0, 0)
        return self.ans


s = Solution()
print(s.countMaxOrSubsets([3,2,1,5]))
