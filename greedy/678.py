# 678. 有效的括号字符串

class Solution:
    def checkValidString(self, s: str) -> bool:
        l, r = 0, 0
        for c in s:
            if c == "(":
                l += 1
                r += 1
            elif c == ")":
                l -= 1
                r -= 1
            elif c == "*":
                l -= 1
                r += 1
            l = max(l, 0)
            if l > r:
                return False
        return l == 0

    def _checkValidString(self, s: str) -> bool:
        q1 = []
        q2 = []
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                q1.append(i)
            elif c == "*":
                q2.append(i)
            elif c == ")":
                if q1:
                    q1.pop()
                elif q2:
                    q2.pop()
                else:
                    return False
        if q1:
            q1_len = len(q1)
            q2_len = len(q2)
            for i in range(q1_len - 1, -1, -1):
                l, r = 0, q2_len - 1
                while l <= r:
                    mid = (l + r) >> 1
                    if q2[mid] > q1[i]:
                        r = mid - 1
                    else:
                        l = mid + 1
                if q2_len - l < q1_len - i:
                    return False
        return True

s = Solution()
print(s.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))