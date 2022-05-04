# 824. 山羊拉丁文


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ws = sentence.split(" ")
        ans = []
        for i in range(len(ws)):
            w = ws[i]
            if w[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                w = w + 'ma'
            else:
                w = w[1:] + w[0] + 'ma'
            w += 'a' * (i + 1)
            ans.append(w)
        return ' '.join(ans)

s = Solution()
print(s.toGoatLatin("I speak Goat Latin"))