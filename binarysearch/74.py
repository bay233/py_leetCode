# 74. 搜索二维矩阵

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        i, j = 0, len(matrix) - 1
        while i <= j:
            mid = (i + j) // 2
            if matrix[mid][0] > target:
                j = mid - 1
            elif matrix[mid][0] < target:
                i = mid + 1
            else:
                return True

        row = (i + j) // 2
        i, j = 0, len(matrix[0]) - 1
        while i <= j:
            mid = (i + j) // 2
            if matrix[row][mid] > target:
                j = mid - 1
            elif matrix[row][mid] < target:
                i = mid + 1
            else:
                return True
        return False


s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
