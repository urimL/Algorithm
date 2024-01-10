import sys
import heapq

input = sys.stdin.readline

n = int(input())
left, right = [], []
for i in range(n):
    x = int(input())

    if len(right) == len(left):
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)

    if right and -left[0] > right[0]:
        leftvalue = heapq.heappop(left)
        rightvalue = heapq.heappop(right)

        heapq.heappush(left, -rightvalue)
        heapq.heappush(right, -leftvalue)

    print(-left[0])
