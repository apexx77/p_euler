def dig_count(n) :
    c = 1
    while n//10 != 0 :
        c += 1
        n = n//10
    return c
k = 1
n = 3
d = 2
ans = 0
while k <= 1000 :
    if dig_count(n) > dig_count(d) :
        ans += 1
    n, d = n+(2*d), n+d
    k += 1
    print(k)
print(ans)


