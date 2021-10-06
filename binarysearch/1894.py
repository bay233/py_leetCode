# 1894. 找到需要补充粉笔的学生编号


List = list

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        arr = [0]
        for c in chalk:
            arr.append(arr[-1] + c)
        idx = k % arr[-1]
        r, l = 1, len(chalk)
        while r <= l:
            mid = (r + l) >> 1
            if arr[mid] >= idx:
                l = mid - 1
            else:
                r = mid + 1
        return l

s = Solution()
print(s.chalkReplacer(chalk = [3,4,1,2], k = 25))