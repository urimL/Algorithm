import sys
input = sys.stdin.readline

n = int(input())
left,right = [0 for _ in range(n)],[0 for _ in range(n)]
nums = list(map(int,input().split()))

left[0] = nums[0]
right[n-1] = nums[n-1]
tmp,result = 0,left[0]

for i in range(1,n):
    left[i] = max(nums[i],left[i-1]+nums[i])
    result = max(result,left[i])

for i in range(n-2,-1,-1):
    right[i] = max(nums[i],right[i+1]+nums[i])

for i in range(1,n-1):
    tmp = left[i-1]+right[i+1]
    result = max(result,tmp)

print(result)