str = ""
arr = [0]
for i in range(20) :
    str = str+input()
for i in range(len(str)-12) :
    p = int(str[i])*int(str[i+1])*int(str[i+2])*int(str[i+3])*int(str[i+4])*int(str[i+5])*int(str[i+6])*int(str[i+7])*int(str[i+8])*int(str[i+9])*int(str[i+10])*int(str[i+11])*int(str[i+12])
    arr.append(p)
print(max(arr))