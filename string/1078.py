# 1078. Bigram 分词

List = list

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ts = text.split(" ")
        n = len(ts)
        if n < 3:
            return []
        ans = []
        for i in range(2, n):
            if ts[i - 2] == first and ts[i - 1] == second:
                ans.append(ts[i])
        return ans


s = Solution()
print(s.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good"))