# 1380. 矩阵中的幸运数


List = list

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> list[float]:
        n, m = len(matrix), len(matrix[0])
        row = [int(10e5)] * n
        col = [0] * m
        for i in range(n):
            for j in range(m):
                row[i] = min(row[i], matrix[i][j])
                col[j] = max(col[j], matrix[i][j])

        ans = []
        for i in range(n):
            if row[i] in col:
                ans.append(row[i])
        return ans

s = Solution()
print(s.luckyNumbers([[56216],[63251],[75772],[1945],[27014]]))


