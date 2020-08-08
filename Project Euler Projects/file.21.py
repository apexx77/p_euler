import math
def prop_div(n) :
    div = 0
    for i in range(1, math.floor(math.sqrt(n))+1) :
        if n%i == 0 :
            if i != n//i :
                div += i+(n//i)
            else :
                div += i
    div -= n
    return div
ans = 0
nums = [n for n in range(1, 10000)]
while nums :
    a = nums.pop(0)
    b = prop_div(a)
    if a == prop_div(b) and a != b :
        ans += a+b
        try :
            nums.remove(b)
        except :
            pass
print(ans)