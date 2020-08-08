arr = []
for i in range(11,100) :
    for j in range(i+1,100) :
        if j//10 != 0 and j%10 != 0 :
            if i/j == (i//10)/(j//10) or i/j == (i//10)/(j%10) or i/j == (i%10)/(j//10) or i/j == (i%10)/(j%10) :
                if i%10 != i//10 :
                    if i%10 == j//10 or i%10 == j%10 or i//10 == j%10 or i//10 == j//10 :
                        arr.extend([i, j])
print(arr)
#After manual filtering from the reuslting list :
#16,64
#19,95
#26,65
#49,98
print((16/64)*(19/95)*(26/65)*(49/98))

