import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
m = int(input())
find = list(map(int,input().split()))

nums.sort()
min_v, max_v = nums[0],nums[n-1]

for i in find:
    check = False
    if min_v<=i<=max_v:
        start,end = 0,n-1
        
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==i:
                check = True
                break
            elif nums[mid]<i:
                start = mid+1
            else:
                end = mid-1
    if check:
        print(1)
    else:
        print(0)
    

