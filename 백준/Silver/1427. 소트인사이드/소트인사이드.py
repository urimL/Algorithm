s=input()
d=[]
for i in range(len(s)):
    d.append(int(s[i]))

d.sort(reverse=True)

for i in range(len(s)):
    print(d[i],end='')
    
