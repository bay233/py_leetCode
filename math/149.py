# 149. 直线上最多的点数

class Solution:
    # def maxPoints(self, points: List[List[int]]) -> int:
    def maxPoints(self, points) -> int:
        res_max = 1
        for i in range(len(points)):
            tmp_book = {}
            for j in range(i + 1, len(points)):
                if not (points[i][0] - points[j][0]):
                    slope = float('inf')
                else:
                    slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                if slope in tmp_book:
                    tmp_book[slope] += 1
                else:
                    tmp_book[slope] = 2
            if tmp_book:
                res_max = max(res_max, max(tmp_book.values()))
        return res_max

s = Solution()
print(s.maxPoints([[1,1],[2,2],[3,3]]))