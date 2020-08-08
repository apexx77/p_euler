arr = [[]]*15
for i in range(15) :
    arr[i] = [int(num) for num in input().split()]
def traversal(array, i, j) :
    if i == 14 :
        return array[i][j]
    else :
        return array[i][j]+max(traversal(array, i+1, j), traversal(array, i+1,j+1))
print(traversal(arr, 0, 0))