# 997. 找到小镇的法官


List = list


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        point = set()
        book = {}
        for t in trust:
            a, b = t[0], t[1]
            if b in book:
                book[b] += 1
            else:
                book[b] = 1
            point.add(a)

        res = 0
        for k, v in book.items():
            if v == n - 1 and k not in point:
                if res == 0:
                    res = k
                else:
                    res = -1
        return res if res else -1

s = Solution()
print(s.findJudge(2, [[1,2]]))


