# 875. 爱吃香蕉的珂珂

class Solution:
    def minEatingSpeed(self, piles: list[int], H: int) -> int:
        def canFinish(piles, speed, H):
            time = 0
            for n in piles:
                time += n // speed + (1 if n % speed > 0 else 0)
            return time <= H


        l = 1
        r = max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            if canFinish(piles, mid, H):
                r = mid - 1
            else:
                l = mid + 1
        return l
