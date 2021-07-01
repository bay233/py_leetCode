

book = {}
def a(n):
    if n == 1 or n == 2:
        return 1
    if book.get(n) != None:
        return book[n]
    res = a(n - 1) + a(n - 2)
    book[n] = res
    return res

def b(n):
    i = 2
    val = int(n)
    while i < val:
        tmp = val
        while tmp > 0:
            tmp = (tmp - 1) / i
            if tmp != int(tmp):
                break
        if not tmp:
            break
        i += 1
    return str(i)


print(format(4681, 'b'))
print(format(13, 'b'))


print(b("1000000000000000000"))