# 942. 增减字符串匹配


List = list


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        r, l = 0, n
        ans = []
        for c in s:
            if c == 'I':
                ans.append(r)
                r += 1
            else:
                ans.append(l)
                l -= 1
        ans.append(r)
        return ans


s = Solution()
print(s.diStringMatch("IDID"))
