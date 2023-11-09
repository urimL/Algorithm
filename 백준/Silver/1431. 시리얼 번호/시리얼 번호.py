tc = int(input())
num = []

for t in range(1,tc+1):
    s = input()
    total = 0
    for i in s:
        if '0'<=i<='9':
            total+=int(i)

    num.append([s,total])
            

num.sort(key=lambda x:(len(x[0]),x[1],x[0]))

for i in num:
    print(i[0])
