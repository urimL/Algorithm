import sys
input = sys.stdin.readline

graph = []
n,m,k = map(int,input().split())
parent = [i for i in range(n+1)]
answer = 0

def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(parent[a])
    b = find(parent[b])

    if a<=b:
        parent[b] = a
    else:
        parent[a] = b

e = list(map(int,input().split()))
for elec in e:
    parent[elec] = 0

for i in range(m):
    u,v,w = map(int,input().split())
    graph.append((u,v,w))

graph.sort(key=lambda x:x[2])

for i in graph:
    u,v,cost = i
    if find(u) != find(v):
        union(u,v)
        answer+=cost

print(answer)