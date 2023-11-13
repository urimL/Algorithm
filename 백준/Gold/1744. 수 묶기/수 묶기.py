import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
plusq = PriorityQueue()
minusq = PriorityQueue()
one,zero,answer = 0,0,0

for _ in range(n):
    data = int(input())
    if data>1:
        plusq.put(data*-1)
    elif data==1:
        one+=1
    elif data==0:
        zero+=1
    else:
        minusq.put(data)


while minusq.qsize()>1:
    data1 = minusq.get()
    data2 = minusq.get()
    answer+=data1*data2

while plusq.qsize()>1:
    data1 = plusq.get()*-1
    data2 = plusq.get()*-1
    answer+=data1*data2


if plusq.qsize()>0:
    answer+=plusq.get()*-1

if minusq.qsize()>0:
    if zero==0:
        answer+=minusq.get()

answer+=one
print(answer)
