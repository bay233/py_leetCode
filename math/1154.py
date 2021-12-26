# 1154. 一年中的第几天


class Solution:
    def dayOfYear(self, date: str) -> int:
        nums = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        f = [0]
        for num in nums:
            f.append(f[-1] + num)

        ss = date.split("-")
        y, m, d = int(ss[0]), int(ss[1]), int(ss[2])
        isleap = (y % 4 == 0 and y % 100 != 100) or y % 400 == 0
        ans = f[m - 1] + 1 if m > 2 and isleap else f[m - 1]
        return ans + d

s = Solution()
print(s.dayOfYear("2019-02-10"))