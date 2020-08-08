import math
def isPythagorean(a, b, c) :
    if (a**2)+(b**2) == (c**2) :
        return 1
    else :
        return 0
for i in range(1, 1000) :
    for j in range(1, 1000) :
        k = math.sqrt((i**2)+(j**2))
        if isPythagorean(i, j, k) == 1 :
            if i+j+k == 1000 :
                print(i*j*k)
                break