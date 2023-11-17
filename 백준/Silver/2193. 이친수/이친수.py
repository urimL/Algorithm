import sys
input = sys.stdin.readline

n = int(input())
answer = 0

count = [[0]*2 for _ in range(n+2)]
count[1][0] = 1
count[2][1] = 1

if 1<=n<=2:
    answer = 1

else:
    for i in range(3,n+1):
        count[i][0] = count[i-1][1]
        count[i][1] = count[i-1][0]+count[i-1][1]
        answer = count[i][0]+count[i][1]

print(answer)