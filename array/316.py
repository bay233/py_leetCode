# 316. 去除重复字母

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        strDict = {}
        for ss in s:
            strDict[ss] = strDict.get(ss, 0) + 1

        res = []
        for ss in s:
            if ss not in res:
                while res and res[-1] > ss and strDict.get(res[-1]) > 0:
                    res.pop()
                res.append(ss)
            strDict[ss] = strDict.get(ss) - 1

        return "".join(res)

s = Solution()
print(s.removeDuplicateLetters("abacb"))