import sys,heapq
input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n):
    num = int(input())
    if num!=0:
        heapq.heappush(heap,(abs(num),num))

    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

