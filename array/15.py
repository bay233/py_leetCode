# 15. 三数之和


class Solution:
    # nums: list[int]
    def threeSum(self, nums):
        if len(nums) < 3: return []
        nums.sort()
        len_nums = len(nums)
        L, i, R = 0, len_nums - 2, len_nums - 1
        res = []
        book = set()
        while i > 0:
            while L < i < R:
                if nums[L] + nums[i] + nums[R] < 0:
                    L += 1
                elif nums[L] + nums[i] + nums[R] > 0:
                    R -= 1
                else:
                    if (nums[L], nums[i], nums[R]) not in book:
                        res.append([nums[L], nums[i], nums[R]])
                        book.add((nums[L], nums[i], nums[R]))
                    L += 1
                    R -= 1
            i -= 1
            L, R = 0, len_nums - 1
        return res


s = Solution()
print(s.threeSum([-2, 0, 1, 1, 2]))
