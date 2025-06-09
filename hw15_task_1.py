def fib_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


count = int(input('How many numbers do you want to generate?'))

for i in fib_generator(count):
    print(i)
