import sys
input = sys.stdin.readline

n = int(input())
d = [[0] for _ in range(n+2)]
d[1],d[2] = 1,2

for i in range(3,n+1):
    d[i] = (d[i-1]+d[i-2])%10007

print(d[n])
