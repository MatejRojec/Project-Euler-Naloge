# 25. naloga
def fibbonacijeve_cifre():
    indeks = 2
    fib_list = [1, 1]
    while len(str(fib_list[-1])) < 1000:
        fib_list.append(fib_list[-1] + fib_list[-2])
        indeks += 1
    return indeks

print(fibbonacijeve_cifre())
4782
