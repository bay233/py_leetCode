# 496. 下一个更大元素 I


List = list

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        n = len(nums2)
        book = {}
        for i in range(n - 1, -1, -1):
            x = nums2[i]
            while stack and stack[-1] <= x:
                stack.pop()
            book[x] = stack[-1] if stack else -1
            stack.append(x)

        res = []
        for num in nums1:
            res.append(book[num])

        return res

s = Solution()
print(s.nextGreaterElement( nums1 = [4,1,2], nums2 = [1,3,4,2]))