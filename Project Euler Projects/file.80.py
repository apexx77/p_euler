from decimal import *
getcontext().prec = 101
arr = []
for i in range(1, 101) :
    a = Decimal(i).sqrt()
    for i in range(len(str(a))) :
        if str(a)[i] == '.' :
            s = int(str(a)[i+1:len(str(a))])
            break
        else :
            s = 0
    ans = 0
    while s//10 != 0 :
        ans += s%10
        s = s//10
    ans += s
    arr.append(ans)
print(sum(arr))
print(arr)


