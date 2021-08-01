# 274. H 指数

class Solution:
    # def hIndex(self, citations: List[int]) -> int:
    def hIndex(self, citations) -> int:
        citations.sort(reverse=True)
        # 可使用二分查找优化
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] >= i + 1:
                return i + 1
        return 0

s = Solution()
print(s.hIndex(citations = [3,0,6,1,5]))