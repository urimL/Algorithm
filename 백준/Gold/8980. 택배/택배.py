import sys
input = sys.stdin.readline

n,c = map(int,input().split())
m = int(input())
box = []
count = [0]*(n+1)
answer = 0

for i in range(m):
    box.append(list(map(int,input().split())))

box.sort(key = lambda x:x[1])

for f,t,s in box:
    tmp = s
    for i in range(f,t):
        if count[i]+tmp > c:
            tmp = c - count[i]

    for i in range(f,t):
        count[i]+=tmp

    answer+=tmp

print(answer)

