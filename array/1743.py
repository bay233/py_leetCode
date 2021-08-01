# 1743. 从相邻元素对还原数组

from collections import defaultdict

class Solution:
    # def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
    def restoreArray(self, adjacentPairs):
        book = defaultdict(int)
        hash_map = defaultdict(list)
        for a, b in adjacentPairs:
            book[a] += 1
            book[b] += 1
            hash_map[a].append(b)
            hash_map[b].append(a)

        head = 0
        for k, v in book.items():
            if v == 1:
                head = k
                break
        n = len(adjacentPairs) + 1
        ans = [0] * n
        ans[0] = head
        ans[1] = hash_map[head][0]
        for i in range(2, n):
            x = ans[i - 1]
            for j in hash_map[x]:
                if j != ans[i - 2]:
                    ans[i] = j
        return ans

s = Solution()
print(s.restoreArray([[-3, -9], [-5, 3], [2, -9], [6, -3], [6, 1], [5, 3], [8, 5], [-5, 1], [7, 2]]))
