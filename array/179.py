# 179. 最大数
import functools


class Solution:
    def largestNumber(self, nums) -> str:
        nums_str = [str(num) for num in nums]

        def key(x, y):
            return int(x + y) - int(y + x)

        key = functools.cmp_to_key(key)
        nums_str.sort(key=key, reverse=True)
        res = ""
        for num in nums_str: res += num
        return str(int(res))


s = Solution()
print(s.largestNumber([34323, 3432]))
