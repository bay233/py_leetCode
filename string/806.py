# 806. 写字符串需要的行数

List = list


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        a = ord('a')
        line = 1
        cur = 0
        for c in s:
            i = ord(c) - a
            cur += widths[i]
            if cur > 100:
                line += 1
                cur = widths[i] if cur % 100 else 0
        return [line, cur]


s = Solution()
print(s.numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))
