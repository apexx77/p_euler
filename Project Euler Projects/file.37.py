import math
def reverse(string) :
    s = ''.join(reversed(string))
    return s
def is_prime(n) :
    if n == 1 :
        return 0
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n%i == 0 :
            return 0
            break
    else :
        return 1
def l_truncatable(n) :
    set = []
    while n//10 != 0 :
        set.append(n)
        n = n//10
    set.append(n)
    for i in set :
        if is_prime(i) == 0 :
            return 0
            break
    else :
        return 1
def r_truncatable(n) :
    n = int(reverse(str(n)))
    set = []
    while n//10 != 0 :
        set.append(int(reverse(str(n))))
        n = n//10
    set.append(n)
    for i in set :
        if is_prime(i) == 0 :
            return 0
            break
    else :
        return 1

arr = []
for i in range(11,1000000) :
    if l_truncatable(i) == 1 and r_truncatable(i) == 1 :
        arr.append(i)
    print(i)
print(arr)
print(sum(arr))

