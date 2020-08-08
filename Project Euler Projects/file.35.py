import math
def is_prime(n) :
    for i in range(2, math.floor(math.sqrt(n))+1) :
        if n%i == 0 :
            return 0
            break
    else :
        return 1
def dig_count(n) :
    c = 1
    while n//10 != 0 :
        c += 1
        n = n//10
    return c
def circulars(n) :
    arr = []
    if dig_count(n) == 1 :
        arr.append(n)
    elif dig_count(n) == 2 :
        arr.extend([n, int(str(n)[1]+str(n)[0])])
    elif dig_count(n) == 3 :
        arr.extend([n, int(str(n)[1:]+str(n)[0]), int(str(n)[2]+str(n)[0:2])])
    elif dig_count(n) == 4 :
        arr.extend([n, int(str(n)[1:]+str(n)[0]), int(str(n)[2:]+str(n)[0:2]), int(str(n)[3]+str(n)[0:3])])
    elif dig_count(n) == 5 :
        arr.extend([n, int(str(n)[1:]+str(n)[0]), int(str(n)[2:]+str(n)[0:2]), int(str(n)[3:]+str(n)[0:3]), int(str(n)[4]+str(n)[0:4])])
    elif dig_count(n) == 6 :
        arr.extend([n, int(str(n)[1:]+str(n)[0]), int(str(n)[2:]+str(n)[0:2]), int(str(n)[3:]+str(n)[0:3]), int(str(n)[4:]+str(n)[0:4]), int(str(n)[5]+str(n)[0:5])])
    return arr
cp = []
for i in range(2, 1000000) :
    for j in circulars(i) :
        if is_prime(j) == 0 :
            break
    else :
        cp.append(i)
    print(i)
print(cp)
print(len(cp))






