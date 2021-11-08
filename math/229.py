# 229. 求众数 II


List = list


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a, b = 0, 0
        c1, c2 = 0, 0
        for num in nums:
            if c1 != 0 and a == num:
                c1 += 1
            elif c2 != 0 and b == num:
                c2 += 1
            elif c1 == 0:
                a = num
                c1 = 1
            elif c2 == 0:
                b = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2 = 0, 0
        for num in nums:
            if num == a:
                c1 += 1
            elif num == b:
                c2 += 1
        res = []
        if c1 > n // 3: res.append(a)
        if c2 > n // 3: res.append(b)
        return res


s = Solution()
print(s.majorityElement([1,1,1,3,3,2,2,2]))
