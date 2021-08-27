# 1583. 统计不开心的朋友

List = list
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        book = [{} for _ in range(n)]
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                book[i][preferences[i][j]] = j

        comb = {}
        for pair in pairs:
            x, y = pair[0], pair[1]
            comb[x] = y
            comb[y] = x

        res = 0
        for i in range(n):
            idx = book[i][comb[i]]
            for j in range(idx):
                r = preferences[i][j]
                if book[r][comb[r]] > book[r][i]:
                    res += 1
                    break

        return res


s = Solution()
print(s.unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]))
