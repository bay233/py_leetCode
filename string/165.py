# 165. 比较版本号

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a1 = version1.split(".")
        a2 = version2.split(".")
        n, m = len(a1), len(a2)
        i = 0
        while i < n or i < m:
            a, b = 0, 0
            if i < n: a = int(a1[i])
            if i < m: b = int(a2[i])
            if a > b: return 1
            elif a < b: return -1
            i += 1
        return 0

s = Solution()
print(s.compareVersion("1.01","1.001"))