import sys

input = sys.stdin.readline

n, m = map(int, input().split())
times = []

for _ in range(n):
    tmp = int(input())
    times.append(tmp)
    
def count(t):
    result = 0
    for time in times:
        result += (t//time)
    return result

start, end = min(times), max(times) * m
answer = end

while start <= end:
    mid = (start + end)  // 2
    if count(mid) >= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
    