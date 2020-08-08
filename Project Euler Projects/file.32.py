import math
def is_9_pandigital(n) :
    arr = []
    while n//10 != 0 :
        if arr.count(n%10) == 0 :
            arr.append(n%10)
        else :
            return 0
        n = n//10
    if arr.count(n) == 0 :
        arr.append(n)
    else :
        return 0
    if arr.count(0) == 0 and len(arr) == 9 :
        return 1
    else :
        return 0
pan = []
for i in range(1000,10000) :
    for j in range(1, math.floor(math.sqrt(i))+1) :
        if i%j == 0 :
            if is_9_pandigital(int(str(i)+str(j)+str(i//j))) == 1 :
                if pan.count(i) == 0 :
                    pan.append(i)
print(sum(pan))























