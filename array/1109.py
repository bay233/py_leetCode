# 1109. 航班预订统计

List = list


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        c = [0] * (n + 1)
        for booking in bookings:
            c[booking[0] - 1] += booking[2]
            c[booking[1]] -= booking[2]

        res = [0] * n
        res[0] = c[0]
        for i in range(1, n):
            res[i] = res[i - 1] + c[i]
        return res

s = Solution()
print(s.corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))