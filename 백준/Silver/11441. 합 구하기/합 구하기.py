import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())

for i in range(n - 1):
    num[i + 1] += num[i]

for _ in range(m):
    s, e = map(int, input().split())
    if s == 1:
        start = 0
    else:
        start = num[s - 2]
    end = num[e - 1]
    print(end - start)
