# 1218. 最长定差子序列


List = list

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        arr_map = {}
        for i in range(n):
            if arr[i] in arr_map:
                arr_map[arr[i]].append(i)
            else:
                arr_map[arr[i]] = [i]

        res = 0
        book = [1 for _ in range(n)]
        for i in range(1, n):
            a = arr[i] - difference
            if a in arr_map:
                for j in arr_map[a]:
                    if j < i:
                        book[i] = max(book[i], book[j] + 1)
            res = max(res, book[i])
        return res


s = Solution()
print(s.longestSubsequence(arr = [4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8], difference = 0))


