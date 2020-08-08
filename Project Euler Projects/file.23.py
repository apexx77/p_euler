import math
def is_abundant(n) :
    prop_div = 0
    for i in range(1, math.floor(math.sqrt(n))+1) :
        if n%i == 0 :
            if i != n//i :
                prop_div+= i+(n//i)
            else :
                prop_div+= i
    prop_div-=n
    if prop_div > n :
        return 1
    else :
        return 0
ar = []
arr = []
for i in range(12, 28124) :
    if is_abundant(i) == 1 :
        ar.append(i)
for i in ar :
    for j in ar[ar.index(i):] :
        if i + j <= 28123:
            if arr.count(i+j) == 0 :
                arr.append(i+j)
        else :
            break
    print(i)
nums = []
for i in range(1, 28123) :
    if arr.count(i) == 0 :
        nums.append(i)
print(sum(nums))