import sys

input = sys.stdin.readline

n, m = map(int, input().split())
p = [int(input()) for _ in range(m)]
p.sort(reverse=True)

price, total = 0, 0

for i in range(m):
    cnt = i + 1
    if i >= n - 1:
        cnt = n

    if total < p[i] * cnt:
        price = p[i]
        total = price * cnt

print(price, total)
