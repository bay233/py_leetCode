# 1190. 反转每对括号间的子串

class Solution:
    def reverseParentheses(self, s: str) -> str:
        deque = []
        for c in s:
            if c == ")":
                tmp = []
                while deque:
                    dc = deque.pop()
                    if dc == "(":
                        for tc in tmp:
                            deque.append(tc)
                        break
                    else:
                        tmp.append(dc)
            else:
                deque.append(c)
        print(deque)
        return "".join(deque)


s = Solution()
print(s.reverseParentheses("a(bcdefghijkl(mno)p)q"))
