import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    c = dict()
    for i in range(n):
        a, b = map(str, input().split())
        if b not in c:
            c[b] = [a]
        else:
            c[b].append(a)

    answer = 1
    for k in c.keys():
        answer *= len(c[k]) + 1

    print(answer - 1)
