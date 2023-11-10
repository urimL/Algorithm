import sys
input = sys.stdin.readline

n,c = map(int,input().split())
msg = list(map(int,input().split()))
count = {}

for i in msg:
    if i not in count.keys():
        count[i]=[1,msg.index(i)]
    else:
        count[i][0]+=1

result = sorted(count.items(),key=lambda x:(-x[1][0],x[1][1]))

for i in result:
    for j in range(i[1][0]):
        print(i[0],end=' ')
