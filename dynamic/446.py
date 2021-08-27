# 446. 等差数列划分 II - 子序列

class Solution:
    # def numberOfArithmeticSlices(self, nums: List[int]) -> int:
    def numberOfArithmeticSlices(self, nums) -> int:
        book = []
        for i in range(len(nums)):
            tmp = {}
            for j in range(i):
                d = nums[i] - nums[j]
                t = book[j]
                cnt = t.get(d, 0)
                cnt += tmp.get(d, 0)
                cnt += 1
                tmp[d] = cnt
            book.append(tmp)

        res = 0
        for b in book:
            for v in b.values():
                res += v

        al, an = 0, len(nums) - 1
        cnt = (al + an) * len(nums) // 2
        return res - cnt