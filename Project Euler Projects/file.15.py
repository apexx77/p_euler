def fact(n) :
    ans = 1
    for i in range(1, n+1) :
        ans*=i
    return ans
a = int(input())
print(fact(2*a)//(fact(a)*fact(a)))