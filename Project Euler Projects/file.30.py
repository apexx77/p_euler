def sum_of_5_prs(n) :
    c = 0
    while n//10 != 0 :
        c+=(n%10)**5
        n = n//10
    c+=n**5
    return c
arr = []
for i in range(2, 1000000) :
    if sum_of_5_prs(i) == i :
        arr.append(i)
    print(i)
print(arr)
print(sum(arr))

