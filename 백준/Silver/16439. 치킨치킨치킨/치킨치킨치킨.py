import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
tmp = [i for i in range(m)]
combs = combinations(tmp, 3)
likes = [list(map(int, input().split())) for _ in range(n)]
result = []

for c in combs:
    tmp = []
    for i in range(n):
        max_like = max(likes[i][c[0]], likes[i][c[1]], likes[i][c[2]])
        tmp.append(max_like)
    result.append(sum(tmp))

print(max(result))
