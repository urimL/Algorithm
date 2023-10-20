import sys
import heapq
input = sys.stdin.readline

n= int(input())
lec=[]

for i in range(n):
    lec.append(list(map(int,input().split())))

lec.sort()
q = []
heapq.heappush(q,lec[0][1])

for i in range(1,n):
    if q[0] <= lec[i][0]:
        heapq.heappop(q)
    heapq.heappush(q,lec[i][1])


print(len(q))
