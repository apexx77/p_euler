from itertools import permutations
import math
def is_prime(n) :
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n%i == 0 :
            return 0
            break
    else :
        return 1
def permutation(n) :
    arr = []
    ar = permutations(n)
    for i in ar :
        arr.append(''.join(i))
    return arr
nums = []
for i in permutation('123') :
    nums.append(int(i))
for i in permutation('1234') :
    nums.append(int(i))
for i in permutation('12345'):
    nums.append(int(i))
for i in permutation('123456') :
    nums.append(int(i))
for i in permutation('1234567') :
    nums.append(int(i))
for i in permutation('12345678') :
    nums.append(int(i))
for i in permutation('123456789') :
    nums.append(int(i))
nums = list(filter(lambda n : is_prime(n) == 1, nums))
print(max(nums))






