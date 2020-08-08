a = []
b = []
arr = []
def is_prime(p) :
    for i in range(2, p-1) :
        if p%i == 0 :
            return 0
            break
    else :
        return 1

for i in range(-999, 1000) :
    for j in range(-1000, 1001) :
        n = 0
        if is_prime((n**2)+(i*n)+(j)) == 1 :
            while is_prime((n**2)+(i*n)+(j)) == 1 :
                n+=1
            arr.append(n)
    print(i, j)
print(max(arr))
