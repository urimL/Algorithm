

n = int(input())
num = list(map(int,input().split()))
start,end = 0,n-1
answer = num[start]+num[end]

while start<end:
    total = num[start]+num[end]
    if abs(answer)>abs(total):
        answer = total

    if total==0:
        break
    elif total>0:
        end -= 1
    else:
        start+=1
    

print(answer)
