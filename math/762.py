# 762. 二进制表示中质数个计算置位

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        nums = [False] * 40
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
            nums[i] = True
        ans = 0
        for i in range(left, right + 1):
            x = i
            cnt = 0
            while x != 0:
                x -= x & -x
                cnt += 1
            if nums[cnt]:
                ans += 1
        return ans
