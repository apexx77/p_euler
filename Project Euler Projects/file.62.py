from itertools import permutations
def is_cube(n) :
    k = n**(1./3.)
    if round(k)**3 == n :
        return 1
    else :
        return 0
def all_permutations(n) :
    ar = []
    i = permutations(str(n))
    for j in i :
        if ar.count(int(''.join(j))) == 0 :
            ar.append(int(''.join(j)))
    return ar
def cube_count(n) :
    count = 0
    arr = []
    for i in all_permutations(n) :
        if is_cube(i) == 1 :
            count += 1
            arr.append(i)
    return arr
for i in range(345, 10000) :
    if len(cube_count(i**3)) >= 5 :
        print(cube_count(i))
    print(i)
