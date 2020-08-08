import math
primes = []
for i in range(2, 1000) :
    for j in range(2, math.floor(math.sqrt(i))+1) :
        if i%j == 0 :
            pass
            break
    else :
        primes.append(i)
def div(n) :
    divisors = []
    for i in range(1, math.floor(math.sqrt(n))+1) :
        if n%i == 0 :
            if i != n//i :
                divisors.extend([i, n//i])
            else :
                divisors.append(i)
    return divisors
def prime_div_count(n) :
    count = 0
    for i in div(n) :
        if primes.count(i) != 0 :
            count += 1
    return count
for i in range(647, 1000000) :
    if prime_div_count(i) == 4 and prime_div_count(i+1) == 4 and prime_div_count(i+2) == 4 and prime_div_count(i+3) == 4 :
        print(i, i+1, i+2, i+3)
        break
    print(i)

