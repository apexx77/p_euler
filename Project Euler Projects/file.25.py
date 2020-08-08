import time
start = time.time()
def fib(n) :
    a = 1
    b = 1
    for i in range(2, n) :
        c = a + b
        a = b
        b = c
    return c
def dig_count(n) :
    count = 1
    while n//10 != 0 :
        count += 1
        n = n//10
    return count
n = 3
while dig_count(fib(n)) < 1000 :
    n += 1
print(n)
print(time.time() - start)