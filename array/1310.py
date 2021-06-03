# 1310. 子数组异或查询

class Solution:
    # def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    def xorQueries(self, arr, queries):
        book_len = len(arr) + 1
        book = [0] * book_len
        tmp = 0
        for i in range(book_len):
            tmp ^= arr[i - 1]
            book[i] = tmp
        res = []
        for querie in queries:
            i = querie[0]
            j = querie[1]
            res.append(book[i] ^ book[j + 1])
        return res

s = Solution()
print(s.xorQueries( [1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
