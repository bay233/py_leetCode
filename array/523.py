# 523. 连续的子数组和

class Solution:
    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    def checkSubarraySum(self, nums, k: int) -> bool:
        book = set()
        sum_val = [0]
        for i in range(len(nums)):
            sum_val.append(sum_val[-1] + nums[i])
        for i in range(2, len(nums) + 1):
            book.add(sum_val[i - 2] % k)
            if sum_val[i] % k in book:
                return True
        return False

    def __checkSubarraySum(self, nums, k: int) -> bool:
        nums_len = len(nums)
        for i in range(1, nums_len + 1):
            tmp = nums[i - 1]
            for j in range(i + 1, nums_len + 1):
                tmp += nums[j - 1]
                if not tmp % k:
                    return True
        return False


s = Solution()
print(s.checkSubarraySum(nums = [0,0], k = 1))
