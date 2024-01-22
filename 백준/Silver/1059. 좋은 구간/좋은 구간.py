import sys

input = sys.stdin.readline

l = int(input())
s = sorted(list(map(int, input().split())))
n = int(input())

start, end = 0, l - 1
left, right = 0, 0
answer = 0

while start <= end:
    mid = (start + end) // 2
    if s[mid] == n:
        answer = -1
        break

    elif s[mid] < n:
        left = s[mid]
        start = mid + 1

    else:
        right = s[mid]
        end = mid - 1

if answer != -1:
    for i in range(left + 1, n + 1):
        if i == n:
            answer += right - n - 1
        else:
            answer += right - n

else:
    answer = 0

print(answer)
