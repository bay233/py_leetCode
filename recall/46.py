# 46. 全排列

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = list()

        def backtrack(nums, track, res):
            if (len(nums) == len(track)):
                res.append(list(track))
                return

            for num in nums:
                if num in track: continue
                track.append(num)
                backtrack(nums, track, res)
                track.remove(num)

        backtrack(nums, [], res)
        return res