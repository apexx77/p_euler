def is_0_9_pandigital(n) :
    ar = []
    while n//10 != 0 :
        if ar.count(n%10) == 0 :
            ar.append(n%10)
        else :
            return 0
        n = n//10
    if ar.count(n) == 0 :
        ar.append(n)
    else :
        return 0
    if  len(ar) == 10 :
        return 1
    else :
        return 0
def prop(n) :
    if int(str(n)[1:4])%2 == 0 and int(str(n)[2:5])%3 == 0 and int(str(n)[3:6])%5 == 0 and int(str(n)[4:7])%7 == 0 and int(str(n)[5:8])%11 == 0 and int(str(n)[6:9])%13 == 0 and int(str(n)[7:])%17 == 0 :
        return 1
    else :
        return 0
from itertools import permutations
def all_permuts(n) :
    nums = []
    ar = permutations(str(n))
    for i in ar :
        if len(str(int(''.join(i)))) == 10 :
            nums.append(int(''.join(i)))
    return nums
arr = []
for i in all_permuts(1234567890) :
    if prop(i) == 1 :
        arr.append(i)
    print(i)
print(arr)
print(sum(arr))

