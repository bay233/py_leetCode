# 397. 整数替换

class Solution:
    def integerReplacement(self, n: int) -> int:
        q = [(n, 0)]
        book = set()
        while q:
            node = q.pop(0)
            val = node[0]
            step = node[1]
            if (val, step) in book:
                continue
            book.add((val, step))
            if val == 1:
                return step
            if val & 1:
                step += 1
                q.append((val - 1, step))
                q.append((val + 1, step))
            else:
                step += 1
                q.append((val // 2, step))
        return 0

s = Solution()
print(s.integerReplacement(7))