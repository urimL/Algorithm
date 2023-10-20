import heapq
import sys

input = sys.stdin.readline
n = []
num = int(input())
answer = 0

for _ in range(num):
    n.append(list(map(int,input().split())))

n.sort(key = lambda x:(x[0],x[1]))
q=[n[0][1]]
start = n[0][0]


for i in range(1,num):
    if q[0]>=n[i][0]:
        if q[0]<n[i][1]:
            heapq.heappop(q)
            heapq.heappush(q,n[i][1])
    else:
        if len(q)>0:
            answer+=(heapq.heappop(q)-start)

        heapq.heappush(q,n[i][1])
        start = n[i][0]

if len(q)>0:
    answer+=(heapq.heappop(q)-start)

print(answer)
