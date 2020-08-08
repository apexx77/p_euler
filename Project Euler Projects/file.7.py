import math
arr = []
for i in range(2, 10000000000) :
    for j in range(2, i) :
        if i%j == 0 :
            break
    else :
        arr.append(i)
    if len(arr) == 10001 :
        print(arr[10000])
        break
