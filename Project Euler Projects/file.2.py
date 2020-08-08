#Even Fibonacci numbers
arr = []
a = 1
b = 2
arr.append(a)
arr.append(b)
c = a+b
while c < 4000000 :
    c = a+b
    a = b
    b = c
    arr.append(c)
arr.pop(-1)
evens = list(filter(lambda n : n%2 == 0, arr))
print(sum(evens))