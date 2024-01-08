import sys

input = sys.stdin.readline
n = int(input())
m = list(map(int, input().split()))
answer = 0

m.sort()
if len(m) % 2 == 0:
    start, end = 0, len(m) - 1
    result = m[start] + m[end]

    while start < end:
        start += 1
        end -= 1
        if result < m[start] + m[end]:
            result = m[start] + m[end]
    answer = result

else:
    start, end = 0, len(m) - 2
    result = m[-1]

    while start < end:
        if result < m[start] + m[end]:
            result = m[start] + m[end]
        start += 1
        end -= 1
    answer = result

print(answer)
