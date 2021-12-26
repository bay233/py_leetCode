# 506. 相对名次

List = list


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        book = [(score[i], i) for i in range(n)]
        book.sort(key=lambda x: x[0], reverse=True)
        res = [''] * n
        for i in range(n):
            if i == 0:
                res[book[i][1]] = 'Gold Medal'
            elif i == 1:
                res[book[i][1]] = 'Silver Medal'
            elif i == 2:
                res[book[i][1]] = 'Bronze Medal'
            else:
                res[book[i][1]] = str(i + 1)
        return res


s = Solution()
print(s.findRelativeRanks([5, 4, 3, 2, 1]))
