import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
bag = []
jewel = []
answer = 0

for _ in range(n):
    m, v = map(int, input().split())
    jewel.append([m, v])

for _ in range(k):
    c = int(input())
    bag.append(c)

bag.sort()
jewel.sort()

hq = []
for b in bag:
    while jewel and jewel[0][0] <= b:
        heapq.heappush(hq, -jewel[0][1])
        heapq.heappop(jewel)

    if hq:
        answer -= heapq.heappop(hq)

print(answer)