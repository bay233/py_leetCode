# 45. 跳跃游戏 II

List = list
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        max_step, end = 0, 0
        step = 0
        for i in range(len(nums) - 1):
            max_step = max(max_step, i + nums[i])
            if i == end:
                step += 1
                end = max_step
        return step