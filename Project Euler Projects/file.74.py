import math
import time
start = time.time()
def fact_sum(n) :
    ans = 0
    while n//10 != 0  :
        ans += math.factorial(n%10)
        n = n//10
    ans += math.factorial(n)
    return ans
key = 0
for n in range(1, 1000000) :
    p = fact_sum(n)
    k = fact_sum(n)
    c = 2
    arr = [n, p]
    while arr.count(fact_sum(p)) == 0 :
        p = fact_sum(p)
        arr.append(p)
        c += 1
        if arr.count(fact_sum(p)) != 0 :
            break
    if c == 60 :
        key += 1
    print(n)
print(key)
print(time.time() - start)