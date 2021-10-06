# 1588. 所有奇数长度子数组的和

List = list

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        sum_arr = [0] * (n + 1)
        for i in range(1, n + 1):
            sum_arr[i] = sum_arr[i - 1] + arr[i - 1]

        res = 0
        for i in range(1, n + 1, 2):
            for j in range(i, n + 1):
                res += sum_arr[j] - sum_arr[j - i]
        return res


s = Solution()
print(s.sumOddLengthSubarrays([10,11,12]))
