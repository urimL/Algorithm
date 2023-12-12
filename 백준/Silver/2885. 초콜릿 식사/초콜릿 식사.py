import sys

input = sys.stdin.readline

n = int(input())
total, count, now = 0, 0, 0
x = [2**i for i in range(21)]
answer = []

for i in x:
    if n<= i:
        total = i
        break

print(total,end=' ')

if n != total:
    while n:
        count+=1
        total //= 2
        if total <= n:
            n-=total

print(count)
