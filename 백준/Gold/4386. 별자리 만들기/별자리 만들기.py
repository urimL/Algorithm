import sys
import math

input = sys.stdin.readline

n = int(input())
star = []
parent = [i for i in range(n+1)]
edge = []
answer = 0


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(x)
    b = find(b)

    if a == b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(n):
    x, y = map(float,input().split())
    star.append([x, y])

for i in range(n-1):
    for j in range(i+1, n):
        edge.append((math.sqrt((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2), i, j))

edge.sort()

for e in edge:
    weight, x, y = e

    if find(x) != find(y):
        union(x, y)
        answer += weight

print(round(answer, 2))