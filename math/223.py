# 223. 矩形面积

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x_sum = abs(ax2 - ax1) + abs(bx2 - bx1)
        y_sum = abs(ay2 - ay1) + abs(by2 - by1)
        x_cur = abs(max(ax1, ax2, bx1, bx2) - min(ax1, ax2, bx1, bx2))
        y_cur = abs(max(ay1, ay2, by1, by2) - min(ay1, ay2, by1, by2))
        x_mx = 0
        if x_cur < x_sum:
            x_mx = x_sum - x_cur
        y_mx = 0
        if y_cur < y_sum:
            y_mx = y_sum - y_cur

        res = abs(ax2 - ax1) * abs(ay2 - ay1) + abs(bx2 - bx1) * abs(by2 - by1)
        if x_mx and y_mx:
            res -= x_mx * y_mx
        return res


s = Solution()
print(s.computeArea(ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2))
