# 930. 和相同的二元子数组

class Solution:
    # def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        pre_sum = [0]
        book = {0:1}
        for num in nums:
            tmp = pre_sum[-1] + num
            pre_sum.append(tmp)
            if tmp in book:
                book[tmp] += 1
            else:
                book[tmp] = 1
        res = 0
        for i in range(len(pre_sum) - 1, -1, -1):
            book[pre_sum[i]] -= 1
            if pre_sum[i] - goal in book:
                res += book[pre_sum[i] - goal]
        return res

s = Solution()
print(s.numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0))

