# 838. 推多米诺

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        b = [0] * n
        cs = ['.'] * n
        q = []
        for i in range(n):
            if dominoes[i] == '.':
                continue
            q.append([i, 1, 1 if dominoes[i] == 'R' else -1])
            cs[i] = dominoes[i]

        while q:
            a = q.pop(0)
            i, time, d, idx = a[0], a[1], a[2], a[0] + a[2]
            if idx < 0 or idx >= n or cs[i] == '.':
                continue
            if b[idx] == 0:
                b[idx] = time + 1
                cs[idx] = 'R' if d == 1 else 'L'
                q.append([idx, b[idx], d])
            elif b[idx] > 1 and b[idx] == time + 1:
                cs[idx] = '.'

        return ''.join(cs)


s = Solution()
print(s.pushDominoes("RR.L"))
