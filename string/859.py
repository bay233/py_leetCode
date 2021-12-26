# 859. 亲密字符串

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        flag = False
        book = [0] * 26
        count = []
        cn = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                count.append(i)
                cn += 1
            idx = ord(s[i]) - ord('a')
            if book[idx]:
                flag = True
            book[idx] = 1
            if cn > 2:
                return False

        if cn == 0 and flag:
            return True
        elif cn == 2:
            return s[count[0]] == goal[count[1]] and s[count[1]] == goal[count[0]]

        return False


s = Solution()
print(s.buddyStrings(s="ba", goal="ab"))
