# 990. 等式方程的可满足性

class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        connected = {}
        def find(a):
            while connected.get(a) and a != connected.get(a):
                connected[a] = connected.get(connected[a], connected[a])
                a = connected[a]
            return a

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            connected[root_a] = root_b

        def is_connected(a, b):
            return find(a) == find(b)

        for equation in equations:
            if equation[1] == "=":
                a, b = equation[0], equation[-1]
                union(a, b)

        for equation in equations:
            if equation[1] == "!":
                a, b = equation[0], equation[-1]
                if is_connected(a, b): return False

        return True


s = Solution()
print(s.equationsPossible(["a==b", "b==c", "d==e", "e==f", "d==a", "f!=a"]))
