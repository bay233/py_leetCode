# 301. 删除无效的括号


List = list


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        count = 0
        stack = 0
        for c in s:
            if c == '(':
                stack -= 1
            elif c == ')':
                if stack:
                    stack += 1
                else:
                    count += 1
        if stack: count += abs(stack)

        n = len(s)
        self.min_step = n - count
        book = set()
        res = set()

        def dp(dept, string, status):
            remain = n - dept
            key = (dept, string)
            if status > 0 or (status + remain) < 0 \
                    or (len(string) + remain) < self.min_step \
                    or key in book:
                return
            if dept == n:
                res.add(string)
                return
            if s[dept] == '(':
                dp(dept + 1, string, status)
                dp(dept + 1, string + s[dept], status - 1)
            elif s[dept] == ')':
                dp(dept + 1, string, status)
                dp(dept + 1, string + s[dept], status + 1)
            else:
                dp(dept + 1, string + s[dept], status)
            book.add(key)

        dp(0, '', 0)
        return list(res)


s = Solution()
print(s.removeInvalidParentheses("()())()"))
