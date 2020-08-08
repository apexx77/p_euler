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
arr = []
for i in range(9001, 9999) :
    if is_9_pandigital(int(str(i)+str(2*i))) == 1 :
        arr.append(int(str(i)+str(2*i)))
print(arr)
print(max(arr))