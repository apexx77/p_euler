#Largest prime factor
from math import  *
def is_prime(n) :
    for i in range(2, ceil(sqrt(n))) :
        if n % i == 0 :
            return 0
    return 1
n = 600851475143
for i in range(2, ceil(sqrt(n))) :
    if n % i == 0 :
        if is_prime(i) :
            max = i
        if is_prime(n//i) :
            if n//i > max :
                max = n//i
print(max)