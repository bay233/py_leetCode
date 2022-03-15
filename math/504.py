# 504. 七进制数

class Solution:
    def convertToBase7(self, num: int) -> str:
        f = 0
        ans = []
        if num < 0:
            f = 1
            num = -num
        while num > 0:
            ans.append(str(num % 7))
            num //= 7
        ans.reverse()
        res = ''.join(ans)
        return '-' + res if f else res


s = Solution()
print(s.convertToBase7(-100))
