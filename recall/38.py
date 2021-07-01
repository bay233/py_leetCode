# 38. 字符串的排列

class Solution:
    # def permutation(self, s: str) -> List[str]:
    def permutation(self, s: str):
        str_len = len(s)
        book = [1] * (str_len + 1)
        book[-1] = 0
        res = set()

        def dp(book, path):
            if book[-1] == str_len:
                res.add("".join(path))
                return

            for i in range(str_len):
                if book[i]:
                    book[i] = 0
                    book[-1] += 1
                    path.append(s[i])
                    dp(book, path)
                    path.pop()
                    book[i] = 1
                    book[-1] -= 1

        dp(book, [])
        return list(res)


s = Solution()
print(s.permutation("abc"))
