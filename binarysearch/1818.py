# 1818. 绝对差值和

class Solution:
    # def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
    def minAbsoluteSumDiff(self, nums1, nums2) -> int:
        sort_num = sorted(nums1)
        def bs(val):
            l, r = 0, len(sort_num) - 1
            while l <= r:
                mid = (r + l) // 2
                if sort_num[mid] >= val:
                    r = mid - 1
                elif sort_num[mid] < val:
                    l = mid + 1
            return r

        res_tmp = 0
        sum_tmp = 0
        for i in range(len(nums1)):
            tmp = abs(nums1[i] - nums2[i])
            sum_tmp += tmp
            index = bs(nums2[i])
            t_tmp = abs(sort_num[index] - nums2[i])
            if index + 1 < len(nums1):
                t_tmp = min(t_tmp, abs(sort_num[index + 1] - nums2[i]))
            if t_tmp < tmp: res_tmp = max(res_tmp, tmp - t_tmp)
        return (sum_tmp - res_tmp) % (10 ** 9 + 7)

s = Solution()
print(s.minAbsoluteSumDiff(nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]))