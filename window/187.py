# 187. 重复的DNA序列


List = list


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []
        book = set()
        res = set()
        for i in range(len(s)):
            c = s[i: i + 10]
            if c in book:
                res.add(c)
            else:
                book.add(c)

        return list(res)


s = Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
