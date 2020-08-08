arr = []
for i in range(1, 1000000) :
    c = 1
    while i>1 :
        if i%2 == 0 :
            i = i//2
            c+=1
        else :
            i = 3*i+1
            c+=1
    arr.append(c)
print(arr.index(max(arr))+1)
