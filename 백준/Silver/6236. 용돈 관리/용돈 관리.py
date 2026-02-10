import sys
input = sys.stdin.readline

n,m = map(int, input().split())
money = []
answer = 0
for _ in range(n):
    money.append(int(input()))

def check(x):
    now, result = 0, 0
    for m in money:
        if x < m:
            return 999999
        if now >= m:
            now -= m
        else:
            now = x - m
            result += 1
    return result
    
start, end = 1, sum(money)
while start <= end:
    mid = (start + end) // 2
    if check(mid) <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)