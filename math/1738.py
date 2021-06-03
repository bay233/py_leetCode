# 1738. 找出第 K 大的异或坐标值

class Solution:
    # def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
    def kthLargestValue(self, matrix, k: int) -> int:
        xor_book = [[0] * (len(matrix[0]) + 1)]
        res = []
        for i in range(len(matrix)):
            tmp = [0]
            for j in range(len(matrix[0])):
                val = tmp[-1] ^ xor_book[i][j+1] ^ xor_book[i][j] ^ matrix[i][j]
                tmp.append(val)
                res.append(val)
            xor_book.append(tmp)
        res.sort(reverse=True)
        return res[k - 1]

s = Solution()
print(s.kthLargestValue( [[5,2],[1,6]], 3))
