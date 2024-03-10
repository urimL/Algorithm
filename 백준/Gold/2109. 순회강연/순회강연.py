import sys
import heapq

input = sys.stdin.readline

n = int(input())
lecture = [list(map(int, input().split())) for _ in range(n)]
lecture.sort(key=lambda x: (x[1], x[0]))

answer, pos = 0, 1
total = []

for l in lecture:
    if not total:
        heapq.heappush(total, l[0])
        pos += 1
    else:
        if pos > l[1]:
            heapq.heappop(total)
            heapq.heappush(total, l[0])
        else:
            heapq.heappush(total, l[0])
            pos += 1

print(sum(total))
