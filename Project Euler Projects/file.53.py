def factorial(n) :
    if n == 1 or n == 0 :
        return 1
    else :
        return n*factorial(n-1)
def nCr(n, r) :
    if r <= n :
        return (factorial(n))//(factorial(n-r)*factorial(r))
    else :
        return 0
ans = 0
for i in range(1, 101):
    for j in range(1, i+1) :
        if nCr(i, j) > 1000000 :
            ans += 1
print(ans)

