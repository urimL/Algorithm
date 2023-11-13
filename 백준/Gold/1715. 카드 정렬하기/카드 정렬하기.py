import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    pq.put(int(input()))

data1,data2 = 0,0
answer = 0

while pq.qsize()>1:
    data1 = pq.get()
    data2 = pq.get()
    tmp = data1+data2
    answer+=tmp
    pq.put(tmp)

print(answer)

