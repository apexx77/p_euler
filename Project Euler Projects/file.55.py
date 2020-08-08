def is_palindrome(n) :
    if str(n) == str(n)[::-1] :
        return 1
    return 0
def reverse(n) :
    return int(str(n)[::-1])
def is_non_lychrel(n) :
    i = 1
    while i<50 :
        if is_palindrome(n) == 1 :
            return 1
        else :
            n += reverse(n)
        i += 1
    return 0
arr = []
for i in range(1, 10000) :
    if is_non_lychrel(i) == 0 :
        arr.append(i)
    print(i)
print(arr)
print(len(arr))
