import math
arr = []
for i in range(1, 100) :
    for j in range(1, 100) :
        if math.sqrt((i*i)+(j*j)).is_integer() == True :
            arr.extend([i, j, int(math.sqrt((i*i)+(j*j)))])
print(arr)