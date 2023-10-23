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
    if i%k==0:
        answer+=i//k
    elif i%k!=0:
        answer+=i//k+1
    if j%k==0:
        answer+=j//k
    elif j%k!=0:
        answer+=j//k+1

print(answer)
