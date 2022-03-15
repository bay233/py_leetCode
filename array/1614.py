# 1614. 括号的最大嵌套深度

class Solution:
    def maxDepth(self, s: str) -> int:
        q = []
        ans = 0
        for c in s:
            if c == "(":
                q.append(c)
                ans = max(ans, len(q))
            if c == ")":
                q.pop()
        return ans


s = Solution()
print(s.maxDepth("1"))
