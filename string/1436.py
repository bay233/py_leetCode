# 1436. 旅行终点站

List = list

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        l = set()
        r = set()
        for path in paths:
            l.add(path[0])
            r.add(path[1])
        res = r - l
        return res.pop()

s = Solution()
print(s.destCity([["B","C"],["D","B"],["C","A"]]))