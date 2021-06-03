# 1442. 形成两个异或相等数组的三元组数目

class Solution:
    # def countTriplets(self, arr: List[int]) -> int:
    def countTriplets(self, arr) -> int:
        arr_len = len(arr)
        xor_arr = [0]
        for a in arr:
            xor_arr.append(xor_arr[-1] ^ a)
        res = 0
        for i in range(1, arr_len + 1):
            for k in range(i + 1, arr_len + 1):
                if xor_arr[k] ^ xor_arr[i - 1] == 0:
                    res += k - i
        return res

s = Solution()
print(s.countTriplets([7,11,12,9,5,2,7,17,22]))