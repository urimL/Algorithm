import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
answer = 0
for _ in range(n):
    houses.append(int(input()))

houses.sort()
def check(x):
    result = 1
    pos = houses[0]
    for i in range(1, len(houses)):
        h = houses[i]
        if pos + x <= h:
            result += 1
            pos = h
    return (result >= c)
    
start, end = 1, max(houses)-min(houses)
while start <= end:
    mid = (start + end) // 2
    if (check(mid)):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)