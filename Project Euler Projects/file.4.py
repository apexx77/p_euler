arr = []
def reverse(s):
  string = ""
  for i in s:
    string = i + string
  return string
for i in range(999, 0, -1) :
    for j in range(999, 0, -1) :
        a = str(i*j)
        if a == reverse(a) :
            arr.append(int(a))
print(max(arr))