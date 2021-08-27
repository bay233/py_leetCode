# 881. 救生艇

List = list
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0
        while l < r:
            sum_weight = people[l] + people[r]
            if sum_weight <= limit:
                l += 1
            r -= 1
            res += 1
        if l == r: res += 1
        return res

s = Solution()
print(s.numRescueBoats(people = [3,5,3,4], limit = 5))
