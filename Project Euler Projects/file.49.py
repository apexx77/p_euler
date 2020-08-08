import math
from itertools import permutations
def is_prime(n) :
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n%i == 0 :
            return 0
            break
    else :
        return 1
def all_permutations(n) :
    ar = []
    i = permutations(str(n))
    for j in i :
        if ar.count(int(''.join(j))) == 0 :
            ar.append(int(''.join(j)))
    return ar
def is_prime_count(n) :
    count = 0
    for i in all_permutations(n) :
        if is_prime(i) == 1 :
            count += 1
    return count
for i in range(1001, 9999) :
    if is_prime_count(i) >= 3 :
        arr = []
        for j in all_permutations(i) :
            if is_prime(j) == 1 :
                arr.append(j)
        arr.sort()
        for i in range(len(arr)) :
            for j in range(i+1, len(arr)) :
                if (arr[i]+arr[j])%2 == 0 and arr.count((arr[i]+arr[j])//2) != 0 :
                    if arr[i]//1000 != 0 and arr[j]//1000 != 0 and (arr[i]+arr[j])//2 != 0 :
                        print(arr[i], (arr[i]+arr[j])//2, arr[j])
                        break
                    break









