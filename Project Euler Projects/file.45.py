t = [(i*(i+1))//2 for i in range(1, 100000)]
p = [(i*((3*i)-1))//2 for i in range(1, 100000)]
h = [(i*((2*i)-1)) for i in range(1, 100000)]
arr = []
for i in t :
   if p.count(i) != 0 and h.count(i) != 0 :
       arr.append(i)
   print(i)
print(arr)
