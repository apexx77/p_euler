import math
def is_prime(n) :
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n%i == 0 :
            return 0
            break
    else :
        return 1
primes = []
ans = []
for i in range(2, 1000) :
    if is_prime(i) == 1 :
        primes.append(i)
for i in range(len(primes)) :
    s = primes[i]
    n = 0
    for j in range(i+1, len(primes)) :
        s += primes[j]
        n += 1
        if is_prime(s) == 1 :
            ans.extend([primes[i], s, n])

print(ans)

