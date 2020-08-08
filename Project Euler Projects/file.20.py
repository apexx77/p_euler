import math
def fact(n) :
    if n == 1 :
        return 1
    return n*fact(n-1)
def dig_sum(n) :
    ans = 0
    while n//10 != 0  :
        ans += n%10
        n = n//10
    return ans+n
print(dig_sum(fact(100)))
