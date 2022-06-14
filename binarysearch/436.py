# 436. 寻找右区间


List = list


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        book = [[p[0], i] for i, p in enumerate(intervals)]

        book.sort(key=lambda x: x[0])

        def find(target):
            l, r = 0, n - 1
            while l <= r:
                mid = l + r >> 1
                if book[mid][0] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        ans = []
        for p in intervals:
            l = find(p[1])
            if l >= n:
                ans.append(-1)
                continue
            ans.append(book[l][1])

        return ans

s = Solution()
print(s.findRightInterval([[1,4],[2,3],[3,4]]))