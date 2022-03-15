# 825. 适龄的朋友

import math

List = list


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        n = 130
        book = [0] * 130
        for age in ages:
            book[age] += 1
        for i in range(1, n):
            book[i] += book[i - 1]

        def check(x, y):
            if y <= 0.5 * x + 7:
                return False
            if y > x:
                return False
            if y > 100 and x < 100:
                return False
            return True

        ans = 0
        x, y = 1, 0
        while y < n - 1:
            y += 1
            a = book[y] - book[y - 1]
            if a == 0:
                continue
            if x < y:
                x = y
            while x < n and check(x, y):
                x += 1
            b = book[x - 1] - book[y - 1] - 1
            if b > 0:
                ans += b * a
        return ans



s = Solution()
print(s.numFriendRequests([16,17,18]))