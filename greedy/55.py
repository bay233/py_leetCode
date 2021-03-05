# 55. 跳跃游戏

List = list
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0
        for i in range(len(nums)):
            max_step = max(max_step, i + nums[i])
            if max_step >= len(nums) - 1:
                return True
            if max_step <= i:
                return False

        return max_step >= len(nums) - 1