import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

answer, start, end = 0,0,1

while start<=end and end<=n:
    total = sum(nums[start:end])

    if total < m:
        end+=1
    elif total > m:
        start+=1
    else:
        answer+=1
        end+=1

print(answer)