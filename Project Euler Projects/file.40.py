const = 0.1
for i in range(2, 1000000) :
    const = str(const)+str(i)
s = str(const)
print(int(s[2])*int(s[11])*int(s[101])*int(s[1001])*int(s[10001])*int(s[100001])*int(s[1000001]))