# 594. 最长和谐子序列

List = list

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        book = {}
        res_max = 0
        for n in nums:
            if n in book:
                book[n][0] += 1
                book[n][1] += 1
                if book[n][2]:
                    res_max = max(book[n][0], book[n][1], res_max)
            else:
                book[n] = [1, 1, 0]
            if n + 1 in book:
                book[n + 1][1] += 1
                book[n + 1][2] = 1
                res_max = max(book[n + 1][1], res_max)
            if n - 1 in book:
                book[n - 1][0] += 1
                book[n - 1][2] = 1
                res_max = max(book[n - 1][0], res_max)
        return res_max

s = Solution()
print(s.findLHS([2,1,1,1,1]))