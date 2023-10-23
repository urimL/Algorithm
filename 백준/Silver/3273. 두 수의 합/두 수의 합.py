import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
x = int(input())
nums.sort()
cnt=0

for i in range(len(nums)):
    start,end = i+1,len(nums)-1
    while start<=end:
        mid = (start+end)//2
        if nums[i]+nums[mid]==x:
            cnt+=nums[start:end+1].count(x-nums[i])
            break
        elif nums[i]+nums[mid]<x:
            start = mid+1
        else:
            end = mid - 1
    
print(cnt)
