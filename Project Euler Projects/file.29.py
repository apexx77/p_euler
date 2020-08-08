arr = []
for i in range(2, 6) :
    for j in range(2, 6) :
        if arr.count(i**j) == 0 :
            arr.append(i**j)
print(len(arr))