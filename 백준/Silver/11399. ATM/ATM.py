n=int(input())
arr=input().split()
result = 0

for i in range(n):
    arr[i]=int(arr[i])

arr.sort()

for i in range(n-1,-1,-1):
    result = result+arr[i]*(n-i)

print(result)
