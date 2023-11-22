import sys
input = sys.stdin.readline

graph = []
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
answer,end_cost = 0,0


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(parent[x])
    y = find(parent[y])

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for i in range(m):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

graph.sort(key=lambda x: x[2])

for i in graph:
    u, v, cost = i
    if find(u) != find(v):
        union(u, v)
        answer += cost
        end_cost = cost

print(answer-end_cost)