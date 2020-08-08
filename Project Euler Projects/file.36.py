def is_palindrome(n) :
    p = int(''.join(reversed(str(n))))
    if p == n :
        return 1
    else :
        return 0
def binary(n) :
    ar = []
    while n//2 != 0 :
        ar.append(n%2)
        n = n//2
    ar.append(n)
    ar.reverse()
    b = ''
    for i in ar :
        b += str(i)
    return int(b)
arr = []
for i in range(1, 1000000) :
    if is_palindrome(i) == 1 and is_palindrome(binary(i)) == 1 :
        arr.append(i)
    print(i)
print(arr)
print(sum(arr))

