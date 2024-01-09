import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []
answer = 0

for _ in range(n):
    d, l = map(int, input().split())
    arr.append([d,l])

arr.sort()
q = []

for d,l in arr:
    heapq.heappush(q, l)
    if d < len(q):
        heapq.heappop(q)

print(sum(q))

