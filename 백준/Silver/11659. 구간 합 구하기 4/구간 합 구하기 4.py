import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))
total = [0]
sum = 0

for j in range(0, n):
    sum += nums[j]
    total.append(sum)

for i in range(m):
    start,end = map(int,input().split())

    print(total[end]-total[start-1])
