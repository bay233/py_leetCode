# 765. 情侣牵手

class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        connected = {}

        def find(a):
            while connected.get(a) != None and a != connected.get(a):
                if connected.get(connected[a]) != None:
                    connected[a] = connected.get(connected[a])
                a = connected[a]
            return a

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            connected[root_a] = root_b

        res = 0
        for r in range(0, len(row), 2):
            if abs(row[r] - row[r + 1]) == 1 and min(row[r], row[r + 1]) % 2 == 0: continue

            half1 = row[r] + 1 if row[r] % 2 == 0 else row[r] - 1
            half2 = row[r + 1] + 1 if row[r + 1] % 2 == 0 else row[r + 1] - 1
            union(row[r + 1], row[r])
            if connected.get(half1) != None and connected.get(half2) != None:
                if find(half1) != find(half2):
                    res += 1
                union(row[r], half1)
                union(row[r + 1], half2)
                res += 1
            elif connected.get(half1) != None or connected.get(half2) != None:
                leader = find(half1) if connected.get(half1) != None else find(half2)
                union(row[r], leader)
                union(row[r + 1], leader)
                res += 1
            else:
                union(row[r], row[r])

        return res


s = Solution()
print(s.minSwapsCouples([1, 4, 0, 5, 8, 7, 6, 3, 2, 9]))