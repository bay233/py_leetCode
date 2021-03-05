# 1011. 在 D 天内送达包裹的能力

class Solution:
    def shipWithinDays(self, weights: list[int], D: int) -> int:
        def canFinish(weights, cap, D):
            day = 1
            ws = 0
            for weight in weights:
                ws += weight
                if ws > cap:
                    day += 1
                    ws = weight
            return day <= D

        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = l + (r - l) // 2
            if canFinish(weights, mid, D):
                r = mid - 1
            else:
                l = mid + 1
        return l