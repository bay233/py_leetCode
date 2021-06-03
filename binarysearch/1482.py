# 1482. 制作 m 束花所需的最少天数

class Solution:
    # bloomDay: List[int]
    def minDays(self, bloomDay, m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        min_day = min(bloomDay)
        max_day = max(bloomDay)

        def chek(bloomDay, day, k, m):
            count_m = 0
            count_day = 0
            for bloom in bloomDay:
                if bloom <= day:
                    count_day += 1
                    if count_day == k:
                        count_m += 1
                        count_day = 0
                else:
                    count_day = 0
            return True if count_m >= m else False

        r, l = min_day, max_day
        while r <= l:
            mid = (r + l) // 2
            if chek(bloomDay, mid, k, m):
                l = mid - 1
            else:
                r = mid + 1
        return r

s = Solution()
print(s.minDays([7,7,7,7,12,7,7], 2, 3))
