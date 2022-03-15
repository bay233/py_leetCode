# 1576. 替换所有的问号

class Solution:
    def modifyString(self, s: str) -> str:
        a = ord("a")
        z = ord("z")
        n = len(s)
        def dfs(i, pre):
            if i == n:
                return ""
            if s[i] != "?":
                return s[i] + dfs(i + 1, s[i])

            for j in range(a, z + 1):
                c = chr(j)
                if i > 0 and c == pre:
                    continue
                if i < n - 1 and s[i + 1] != "?" and c == s[i + 1]:
                    continue
                return c + dfs(i + 1, c)

        return dfs(0, "")

s = Solution()
print(s.modifyString("j?qg??b"))