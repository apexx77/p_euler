def digits(n) :
    arr = []
    while n//10 != 0 :
        arr.append(n%10)
        n = n//10
    arr.append(n)
    arr.sort()
    return arr
for i in range(1, 1000000) :
    if digits(i) == digits(2*i) == digits(3*i) == digits(4*i) == digits(5*i) == digits(6*i) :
        print(i)
        break


