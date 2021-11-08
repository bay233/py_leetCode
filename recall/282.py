# 282. 给表达式添加运算符

List = list

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        num_len = len(num)
        self.res = []

        def dp(n, pre_op, pre_n, cur_sum, path):
            if n == num_len:
                if cur_sum == target:
                    self.res.append(path[1:])
                return

            for i in range(n, num_len):
                cur = int(num[n: i + 1])
                s_cur = str(cur)
                if len(s_cur) != i + 1 - n:
                    continue
                dp(i + 1, '+', cur, cur_sum + cur, path + '+' + s_cur)
                if path != '':
                    dp(i + 1, '-', cur, cur_sum - cur, path + '-' + s_cur)
                if pre_op == '+':
                    dp(i + 1, pre_op, pre_n * cur, (cur_sum - pre_n) + pre_n * cur, path + '*' + s_cur)
                elif pre_op == '-':
                    dp(i + 1, pre_op, pre_n * cur, (cur_sum + pre_n) - pre_n * cur, path + '*' + s_cur)

        dp(0, '', 0, 0, '')
        return self.res

s = Solution()
print(s.addOperators(num = "232", target = 8))