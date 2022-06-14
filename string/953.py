# 953. 验证外星语词典

import functools

List = list


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        book = {}
        for i in range(26):
            book[order[i]] = i

        def sort_key(x, y):
            n, m = len(x), len(y)
            i = 0
            r = min(n, m)
            while i < r:
                if book[x[i]] < book[y[i]]:
                    return -1
                elif book[x[i]] > book[y[i]]:
                    return 1
                i += 1
            if n < m:
                return -1
            else:
                return 1

        res = sorted(words, key=functools.cmp_to_key(sort_key))
        for i in range(len(words)):
            if res[i] != words[i]:
                return False
        return True


s = Solution()
print(s.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
