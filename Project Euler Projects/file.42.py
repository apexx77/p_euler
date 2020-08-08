arr1 = []
for i in range(1, 1000) :
    arr1.append((i*(i+1))//2)
vals = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 26
}
arr3 = []
arr2 = [str(name) for name in input().split(",")]
for i in arr2 :
    i = i[1:len(i)-1]
    val = 0
    for j in i :
        val += vals[j]
    arr3.append(val)
ans = 0
for i in arr3 :
    if arr1.count(i) != 0 :
        ans += 1
print(ans)

