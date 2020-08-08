import math
def is_prime(n) :
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n%i == 0 :
            return 0
            break
    else :
        return 1
nums = [i for i in range(2, 10000)]
composites =  list(filter(lambda n : is_prime(n) == 0, nums))
primes = list(filter(lambda n : is_prime(n) == 1, nums))
arr = []
for i in composites :
    for j in primes :
        if i > j :
            if (i-j)%2 == 0 :
                if str(math.sqrt((i-j)//2)).isdigit() == True :
                    arr.append(i)
                    break
    print(i)
print(arr)

