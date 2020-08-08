import math
def combinations(a, b, c, d, e) :
    ar = []
    ar.extend([int(str(a)+str(b)), int(str(a)+str(c)), int(str(a)+str(d)), int(str(a)+str(e)), int(str(b)+str(a)), int(str(b)+str(c)), int(str(b)+str(d)), int(str(b)+str(e)), int(str(c)+str(a)), int(str(c)+str(b)), int(str(c)+str(d)), int(str(c)+str(e)), int(str(d)+str(a)), int(str(d)+str(b)), int(str(d)+str(c)), int(str(d)+str(e)), int(str(e)+str(a)), int(str(e)+str(b)), int(str(e)+str(c)), int(str(e)+str(d))])
    return ar
def is_prime(n) :
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n%i == 0 :
            return 0
            break
    else :
        return 1
primes = []
for i in range(2, 1000) :
    if is_prime(i) == 1 :
        primes.append(i)
ans = []
for i in range(len(primes)) :
    for j in range(i+1, len(primes)) :
        for k in range(j+1, len(primes)) :
            for l in range(k+1, len(primes)) :
                for m in range(l+1, len(primes)) :
                    for p in combinations(primes[i], primes[j], primes[k], primes[l], primes[m]) :
                        if is_prime(p) == 0 :
                            break
                    else :
                        ans.extend([primes[i], primes[j], primes[k], primes[l], primes[m]])
    print(i)
print(ans)