nums = [(n*((3*n)-1))//2 for n in range(1000, 2500)]
arr = []
for i in range(len(nums)) :
    for j in range(i+1, len(nums)) :
        if nums.count(nums[i]+nums[j]) != 0 and nums.count(abs(nums[i]-nums[j])) != 0 :
            arr.extend([nums[i], nums[j]])
    print(i)
print(arr)
