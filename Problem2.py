def fibo(num):
    a,b = 1, 2
    for i in range(0, num):
        yield "{}".format(a)
        a, b = b, a + b
for item in fibo(10):
    count = 0
    if item%2==0:
        count += item
