# 71. 简化路径


class Solution:
    def simplifyPath(self, path: str) -> str:
        ps = path.split("/")
        res = []
        for p in ps:
            if p == "" or p == ".":
                continue
            if p == "..":
                if res:
                    res.pop()
                continue
            res.append(p)
        return "/" + "/".join(res)

s = Solution()
print(s.simplifyPath("/home/../foo/"))
