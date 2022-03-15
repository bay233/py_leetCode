# 917. 仅仅反转字母

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        b = list(s)
        a, z = ord('a'), ord('z')
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and (ord(b[l].lower()) > z or ord(b[l].lower()) < a):
                l += 1
            while l < r and (ord(b[r].lower()) > z or ord(b[r].lower()) < a):
                r -= 1
            if l < r:
                b[l], b[r] = b[r], b[l]
                l += 1
                r -= 1
        return ''.join(b)

s = Solution()
print(s.reverseOnlyLetters("7_28]"))