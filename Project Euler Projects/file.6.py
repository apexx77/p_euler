n = int(input())
a = n*(n+1)//2
b = 0
for i in range(1, n+1) :
    b = b+(i**2)
print((a**2)-b)