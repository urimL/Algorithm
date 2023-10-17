n = int(input())
k = []
answer,start = 0,0

for i in range(n):
    k.append(list(map(int,input().split())))

k.sort(key=lambda x:(x[1],x[0]))

for i in k:
    if start <= i[0]:
        answer+=1
        start = i[1]

print(answer)
