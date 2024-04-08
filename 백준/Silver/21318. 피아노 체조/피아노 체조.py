import sys

input = sys.stdin.readline

n = int(input())
level = list(map(int, input().split()))
q = int(input())

tmp = [0] * (n + 1)
for i in range(1, n):
    if level[i - 1] <= level[i]:
        tmp[i] = tmp[i - 1]

    else:
        tmp[i] = tmp[i - 1] + 1

    if i == n - 1:
        tmp[n] = tmp[i]

for _ in range(q):
    x, y = map(int, input().split())
    print(tmp[y - 1] - tmp[x - 1])
