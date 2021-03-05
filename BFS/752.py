# 752. 打开转盘锁

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if '0000' in deadends: return -1
        q = [['0000']]
        step = 0
        mome = set(deadends)

        while len(q) > 0:
            qs = q.pop(0)
            new_q = []
            for ss in qs:
                if ss == target:
                    return step
                for index, s in enumerate(ss):
                    for i in [11, 9]:
                        add = str((int(s) + i) % 10)
                        temp = ss[:index] + add + ss[index+1:]
                        if temp not in mome:
                            new_q.append(temp)
                            mome.add(temp)
            if (len(new_q) > 0):
                q.append(new_q)
            step += 1

        return -1


s = Solution()
print(s.openLock(["0000"],"8888"))