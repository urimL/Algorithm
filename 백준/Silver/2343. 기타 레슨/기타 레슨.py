import sys

input = sys.stdin.readline

n, m = map(int,input().split())
bluray = list(map(int, input().split()))
start, end = 1, sum(bluray)
answer = 0

while start <= end:
    mid = (start+end)//2
    cnt, total = 1, 0
    for i in bluray:
        if i > mid:
            cnt = -1
            break
        total += i
        if total > mid:
            total = i
            cnt += 1

    if cnt > m or cnt == -1:
        start = mid+1
    else:
        answer = mid
        end = mid-1

print(answer)
