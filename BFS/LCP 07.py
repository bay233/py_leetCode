# LCP 07. 传递信息

class Solution:
    # def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
    def numWays(self, n: int, relation, k: int) -> int:
        relation_dict = {}
        for r in relation:
            if r[0] in relation_dict:
                relation_dict[r[0]].append(r[1])
            else:
                relation_dict[r[0]] = [r[1]]

        queue = [[0]]
        frequency = 0
        res = 0
        while queue:
            if frequency > k: return res
            level = queue.pop()
            tmp_level = []
            while level:
                people = level.pop()
                if frequency == k and people == n - 1:
                    res += 1
                elif people in relation_dict:
                    tmp_level.extend(relation_dict[people])
            if tmp_level: queue.append(tmp_level)
            frequency += 1
        return res

s = Solution()
print(s.numWays(n = 3, relation = [[0,2],[2,1]], k = 2))