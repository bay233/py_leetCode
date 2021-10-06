# 414. 第三大的数

List = list

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a1, a2, a3 = float('-inf'), float('-inf'), float('-inf')
        book = set()
        for num in nums:
            if num in book:
                continue
            book.add(num)
            if num > a1:
                a1, a2, a3 = num, a1, a2
            elif num > a2:
                a2, a3 = num, a2
            elif num > a3:
                a3 = num
        return a3 if a1 != a3 and a2 != a3 and a3 != float('-inf') else a1


s = Solution()
print(s.thirdMax([2,2,3,1]))