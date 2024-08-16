import heapq
import sys

input = sys.stdin.readline
n = int(input())
hq = []
nums = []
answer = 0

for i in range(n):
    d, r = map(int, input().split())
    nums.append([d,r])

nums.sort()

for d,r in nums:
    heapq.heappush(hq, r)
    if d < len(hq):
        heapq.heappop(hq)

print(sum(hq))