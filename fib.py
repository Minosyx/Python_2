def fib():
    fib.a, fib.b = fib.b, fib.a + fib.b
    return fib.a

fib.a = 0
fib.b = 1


for i in range(10):
    print(fib())