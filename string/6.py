# 6. Z 字形变换


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        book = [[] for _ in range(numRows)]

        n = len(s)
        i = 0
        while i < n:
            j = 0
            while j < numRows and i < n:
                book[j].append(s[i])
                i += 1
                j += 1
            if numRows > 2:
                j = numRows - 2
                while j > 0 and i < n:
                    book[j].append(s[i])
                    i += 1
                    j -= 1
        ans = ''
        for b in book:
            ans += ''.join(b)
        return ans


s = Solution()
print(s.convert("PAYPALISHIRING", numRows=4))
