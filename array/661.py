# 661. 图片平滑器


List = list


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        ans = [[0] * m for _ in range(n)]
        step = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for i in range(n):
            for j in range(m):
                sum_v = img[i][j]
                sum_c = 1
                for s in step:
                    x, y = i + s[0], j + s[1]
                    if x < 0 or x >= n or y < 0 or y >= m:
                        continue
                    sum_v += img[x][y]
                    sum_c += 1
                ans[i][j] = sum_v // sum_c
        return ans


s = Solution()
print(s.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
