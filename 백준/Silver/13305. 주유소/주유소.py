import sys
import heapq

input = sys.stdin.readline

n = int(input())
road = list(map(int,input().split()))
price = list(map(int,input().split()))
result = []
min_price = price[0]

for i in range(n-1):
    if i==0:
        result.append(road[i]*price[i])
        continue

    if min_price>price[i]:
        min_price = price[i]
    result.append(min_price*road[i])

print(sum(result))


