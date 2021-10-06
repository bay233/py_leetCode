# 447. 回旋镖的数量

import math

List = list


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        book = []
        n = len(points)
        for i in range(n):
            tmp = {}
            for j in range(n):
                dis = math.sqrt(pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2))
                if dis in tmp:
                    tmp[dis] += 1
                else:
                    tmp[dis] = 1
            book.append(tmp)
        res = 0
        for b in book:
            for v in list(b.values()):
                if v >= 2:
                    res += v * (v - 1)
        return res

s = Solution()
print(s.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))
