import sys
input = sys.stdin.readline

n = int(input())
d = [0 for _ in range(n)]
nums = list(map(int,input().split()))

d[0] =  nums[0]

for i in range(1,n):
    d[i] = max(nums[i],d[i-1]+nums[i])

print(max(d))