n=int(input())
arr=list(map(int,input().split()))
lis = [arr[0]]

def binary(e):
    start = 0
    end = len(lis)-1

    while start<=end:
        mid = (start+end)//2

        if lis[mid]==e:
            return mid
        elif lis[mid]<e:
            start=mid+1
        else:
            end = mid-1
    return start

for i in range(n):
    if arr[i]>lis[-1]:
        lis.append(arr[i])
    else:
        lis[binary(arr[i])] = arr[i]

print(len(lis))
