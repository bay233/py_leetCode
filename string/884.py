# 884. 两句话中的不常见单词

List = list


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        b1 = {}
        b2 = {}
        ss1 = s1.split(" ")
        for s in ss1:
            b1[s] = b1.get(s, 0) + 1
        ss2 = s2.split(" ")
        for s in ss2:
            b2[s] = b2.get(s, 0) + 1
        ans = []
        for k, v in b1.items():
            if v == 1 and k not in b2:
                ans.append(k)
        for k, v in b2.items():
            if v == 1 and k not in b1:
                ans.append(k)
        return ans


s = Solution()
print(s.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))