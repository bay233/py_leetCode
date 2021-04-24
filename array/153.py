# 153. 寻找旋转排序数组中的最小值

class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1
        res_min = float('inf')
        while left <= right:
            mid = (left + right) // 2
            res_min = nums[mid] if nums[mid] < res_min else res_min
            # 左边有序
            if nums[left] <= nums[mid]:
                if nums[left] <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右边有序
            else:
                if nums[left] >= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return res_min

s = Solution()
print(s.findMin([6,7,0,1,2,4,5]))