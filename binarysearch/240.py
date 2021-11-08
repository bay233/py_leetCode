# 240. 搜索二维矩阵 II


List = list


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        l, r = 0, min(m, n)
        while l <= r:
            mid = l + r >> 1
            if matrix[mid][mid] > target:
                r -= 1
            elif matrix[mid][mid] < target:
                l += 1
            else:
                return True

        point = r
        i = point
        while i <= m:
            l, r = 0, n
            while l <= r:
                mid = l + r >> 1
                if matrix[i][mid] > target:
                    r -= 1
                elif matrix[i][mid] < target:
                    l += 1
                else:
                    return True
            i += 1

        i = point
        while i <= n:
            l, r = 0, m
            while l <= r:
                mid = l + r >> 1
                if matrix[mid][i] > target:
                    r -= 1
                elif matrix[mid][i] < target:
                    l += 1
                else:
                    return True
            i += 1

        return False


s = Solution()
print(s.searchMatrix(
    [[4, 9, 9, 11, 12, 15, 17, 22, 23],
     [8, 10, 11, 14, 14, 17, 20, 23, 26],
     [9, 13, 16, 21, 23, 26, 30, 35, 36],
     [9, 14, 18, 21, 26, 29, 32, 35, 39],
     [12, 18, 19, 23, 27, 33, 34, 37, 39],
     [15, 20, 24, 26, 32, 34, 36, 39, 42],
     [16, 24, 28, 28, 33, 37, 37, 43, 44],
     [18, 28, 28, 29, 35, 42, 44, 49, 52],
     [23, 32, 34, 34, 39, 46, 51, 51, 56],
     [27, 35, 35, 40, 45, 47, 51, 55, 58]], target=30))
