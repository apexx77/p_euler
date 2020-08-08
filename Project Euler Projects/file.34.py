def fact(n) :
    if n == 1 or n ==0 :
        return 1
    return n*fact(n-1)
def digits(n) :
    dig = []
    while n//10 != 0 :
        dig.append(n%10)
        n = n//10
    dig.append(n)
    return dig
arr = []
for i in range(10,100000) :
    sum = 0
    for j in digits(i) :
        sum+=fact(j)
    if i == sum :
        arr.append(i)
    print(i)
print(arr)


