

book = {}
def a(n):
    if n == 1 or n == 2:
        return 1
    if book.get(n) != None:
        return book[n]
    res = a(n - 1) + a(n - 2)
    book[n] = res
    return res


print(a(100))