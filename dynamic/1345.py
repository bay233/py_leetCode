# 1345. 跳跃游戏 IV


List = list


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        book = {}
        n = len(arr)
        if n == 1: return 0
        for i in range(n):
            if arr[i] in book:
                book[arr[i]].append(i)
            else:
                book[arr[i]] = [i]

        q = [0]
        s = set()
        ans = 0
        while q:
            tmp = []
            for i in q:
                if i == n - 1:
                    return ans
                if i in s:
                    continue
                s.add(i)
                if i + 1 < n:
                    tmp.append(i + 1)
                if i - 1 >= 0:
                    tmp.append(i - 1)
                if arr[i] in book:
                    for j in book[arr[i]]:
                        if j not in s:
                            tmp.append(j)
                    book.pop(arr[i])
            ans += 1
            if tmp:
                q = tmp
            else:
                break
        return ans


s = Solution()
print(s.minJumps([11,22,7,7,7,7,7,7,7,22,13]))
