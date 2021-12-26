# 318. 最大单词长度乘积

List = list


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        book = []
        for word in words:
            val = 0
            length = 0
            for w in word:
                val |= 1 << (ord(w) - ord("a"))
                length += 1
            book.append((val, length))

        res_max = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if not (book[i][0] & book[j][0]):
                    res_max = max(res_max, book[i][1] * book[j][1])
        return res_max

s = Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))

