# 412. Fizz Buzz

List = list


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        book = [str(_ + 1) for _ in range(n)]
        tmp = 3
        while tmp <= n:
            book[tmp - 1] = 'Fizz'
            tmp += 3

        tmp = 5
        while tmp <= n:
            if book[tmp - 1] == 'Fizz':
                book[tmp - 1] = 'FizzBuzz'
            else:
                book[tmp - 1] = 'Buzz'
            tmp += 5

        return book


s = Solution()
print(s.fizzBuzz(15))
