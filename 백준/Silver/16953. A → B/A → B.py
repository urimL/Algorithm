import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
answer = 1

while m != n:
    if m < n:
        answer = -1
        break

    if m % 2 == 0:
        answer += 1
        m //= 2
    elif m % 10 == 1:
        answer += 1
        m -= 1
        m //= 10
    else:
        answer = -1
        break


print(answer)
