def dig_sq_sum(n) :
    ans = 0
    for i in str(n) :
        ans += int(i)**2
    return ans
def compute(n) :
    while True :
        if dig_sq_sum(n) == 1 or dig_sq_sum(n) == 89 :
            if dig_sq_sum(n) == 89 :
                return 1
            elif dig_sq_sum(n) == 1 :
                return 0
            else :
                n = dig_sq_sum(n)
print(compute(2))

