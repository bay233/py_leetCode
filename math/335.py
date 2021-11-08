# 335. 路径交叉

List = list


class Solution:

    def isSelfCrossing(self, distance: List[int]) -> bool:
        d = distance
        n = len(distance)
        if n < 4: return False
        for i in range(3, n):
            if d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]: return True
            if i >= 4 and d[i - 1] == d[i - 3] and d[i] + d[i - 4] >= d[i - 2]: return True;
            if i >= 5 and d[i - 1] <= d[i - 3] and d[i - 2] > d[i - 4] \
                    and d[i] + d[i - 4] >= d[i - 2] and d[i - 1] + d[i - 5] >= d[i - 3]: return True

        return False