# 969. 煎饼排序


List = list


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        book = [0] * (n + 1)
        for i in range(n):
            book[arr[i]] = i

        def rever(arr, i, j, book):
            while i < j:
                book[arr[i]], book[arr[j]] = j, i
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        ans = []
        for i in range(n, 0, -1):
            idx = book[i]
            if idx == i - 1:
                continue
            if idx != 0:
                ans.append(idx + 1)
                rever(arr, 0, idx, book)
            ans.append(i)
            rever(arr, 0, i - 1, book)
        return ans


s = Solution()
print(s.pancakeSort([3, 2, 4, 1]))
