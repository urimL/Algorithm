import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cables = []
answer = 0
for _ in range(n):
    cables.append(int(input()))

start, end = 1, max(cables)

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for c in cables:
        cnt += c // mid

    if cnt >= m:
        answer = mid
        start = mid + 1

    else:
        end = mid - 1

print(answer)
