# 477. 汉明距离总和

class Solution:
    # def totalHammingDistance(self, nums: List[int]) -> int:
    def totalHammingDistance(self, nums) -> int:
        book = [[0, 0] for _ in range(32)]
        for num in nums:
            for i in range(32):
                if num & 1:
                    book[i][1] = book[i][1] + 1
                else:
                    book[i][0] = book[i][0] + 1
                num >>= 1
        res = 0
        for b in book:
            res += b[0] * b[1]
        return res

s = Solution()
print(s.totalHammingDistance([4, 14, 2]))