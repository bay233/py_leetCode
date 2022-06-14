# 面试题 01.05. 一次编辑


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        n, m = len(first), len(second)
        if abs(m - n) >= 2:
            return False
        l, r1, r2 = 0, n - 1, m - 1
        m_len = min(n, m)
        while l < m_len:
            if first[l] != second[l]:
                break
            l += 1

        while r1 >= l and r2 >= l:
            if first[r1] != second[r2]:
                break
            r1 -= 1
            r2 -= 1

        return max(r1, r2) - l < 1


s = Solution()
print(s.oneEditAway("pales", "paes"))
