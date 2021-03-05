# 128. 最长连续序列

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        return 0

    def union_find(self, nums: list[int]) -> int:
        dicts = {}

        def find(a):
            if connected.get(a) == None or a == connected.get(a):
                return 0
            if dicts.get(a) != None:
                return dicts.get(a)
            length = find(connected.get(a)) + 1
            dicts[a] = length
            return length

        connected = {num: num - 1 for num in nums}

        max_length = 0
        for num in nums:
            max_length = max(max_length, find(num))

        return max_length

s = Solution()
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

