import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().split()))
cards.sort()
m = int(input())
nums = list(map(int,input().split()))

result = {}

for i in nums:
    start,end = 0,n-1
    while start<=end:
        mid = (start+end)//2
        if cards[mid]==i:
            result[i] = '1'
            break
        elif cards[mid]<i:
            start=mid+1
        else:
            end=mid-1


for i in nums:
    if i in result.keys():
        print('1',end=' ')
    else:
        print('0',end=' ')
