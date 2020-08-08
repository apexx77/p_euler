def digit_sum(n) :
    ans = 0
    while n//10 != 0 :
        ans += n%10
        n = n//10
    ans += n
    return ans
arr = []
for i in range(1, 100) :
    for j in range(1, 100) :
        arr.append(digit_sum(i**j))
    print(i)
print(max(arr))