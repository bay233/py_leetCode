# 1036. 逃离大迷宫

List = list

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        step = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        base = 131
        EDGE, MAX = 1e6, 1e5
        blocked_set = set()
        for b in blocked:
            blocked_set.add(b[0] * base + b[1])
        n = len(blocked)
        MAX = n * (n - 1) // 2

        def check(a, b):
            vis = set()
            d = []
            d.append(a)
            vis.add(a[0] * base + a[1])
            while d and len(vis) <= MAX:
                poll = d.pop(0)
                x, y = poll[0], poll[1]
                if x == b[0] and y == b[1]:
                    return True
                for s in step:
                    nx, ny = x + s[0], y + s[1]
                    if nx < 0 or nx >= EDGE or ny < 0 or ny >= EDGE:
                        continue
                    h = nx * base + ny
                    if h in blocked_set:
                        continue
                    if h in vis:
                        continue
                    d.append([nx, ny])
                    vis.add(h)
            return len(vis) > MAX

        return check(source, target) and check(target, source)

s = Solution()
print(s.isEscapePossible(blocked = [[0,3],[1,0],[1,1],[1,2],[1,3]], source = [0,0], target = [0,2]))