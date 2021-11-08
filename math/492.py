# 492. 构造矩形

List = list

import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = int(math.sqrt(area))
        l, r = i, i
        while True:
            mid = l * r
            if mid > area:
                l -= 1
            elif mid < area:
                r += 1
            else:
                return [r, l]


s = Solution()
print(s.constructRectangle(8))
