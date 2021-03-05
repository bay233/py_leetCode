# 986. 区间列表的交集

class Solution:
    def intervalIntersection(self, A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if (A[i][0] <= B[j][1] and A[i][1] >= B[j][0]) or (B[j][0] <= A[i][1] and B[j][1] >= A[i][0]):
                res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])

            if A[i][1] > B[j][1]: j += 1
            else: i+= 1
        return res

s = Solution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))