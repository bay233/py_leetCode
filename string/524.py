# 524. 通过删除字母匹配到字典里最长单词

List = list

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        res = ["", 0]
        for d in dictionary:
            low = 0
            d_len = len(d)
            for c in s:
                if c == d[low]:
                    low += 1
                if low == d_len:
                    if d_len > res[1]:
                        res[0], res[1] = d, d_len
                    elif d_len == res[1]:
                        if res[0] > d:
                            res[0] = d
                    break
        return res[0]

s = Solution()
print(s.findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))