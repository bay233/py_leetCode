# 553. 最优除法


List = list


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        sb = []
        for i in range(n):
            sb.append(str(nums[i]))
            if i + 1 < n:
                sb.append("/")
        if n > 2:
            idx = 0
            for i in range(len(sb)):
                if sb[i] == "/":
                    idx = i
                    break
            sb.insert(idx + 1, "(")
            sb.append(")")
        return "".join(sb)


s = Solution()
print(s.optimalDivision([1000, 100, 10, 2]))
