import sys
input = sys.stdin.readline

girl = [0]*6
boy = [0]*6
answer = 0

n,k = map(int,input().split())
for i in range(n):
    s,y = map(int,input().split())
    if s==0:
        girl[y-1]+=1
    else:
        boy[y-1]+=1


for i,j in zip(girl,boy):
    if i > k:
        answer+=i//k+1
    elif 0<i<=k:
        answer+=1
    if j > k:
        answer+=j//k+1
    elif 0<j<=k:
        answer+=1

print(answer)
