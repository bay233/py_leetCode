# 475. 供暖器

List = list


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        n = len(houses)
        m = len(heaters)

        def check(x):
            j = 0
            for i in range(n):
                while j < m and houses[i] > heaters[j] + x:
                    j += 1
                if j < m and heaters[j] - x <= houses[i] <= heaters[j] + x:
                    continue
                return False
            return True

        l, r = 0, 10 ** 9
        while l < r:
            mid = l + r >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r

s = Solution()
print(s.findRadius(houses = [1,2,3], heaters = [2]))
