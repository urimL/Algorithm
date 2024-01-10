import sys
import heapq

input = sys.stdin.readline

n = int(input())
hw = []
total_deadline = 0

for i in range(n):
    d, w = map(int, input().split())
    heapq.heappush(hw, [-w, d])
    if total_deadline < d:
        total_deadline = d

visited = [False] * (total_deadline + 1)
answer = 0

while hw:
    w, d = heapq.heappop(hw)

    for i in range(d, 0, -1):
        if visited[i]:
            continue

        visited[i] = True
        answer += -w
        break

print(answer)
