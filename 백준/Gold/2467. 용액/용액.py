n = int(input())
num = list(map(int,input().split()))

start, end = 0,n-1
answer = num[start]+num[end]
result_start,result_end = 0,0

while start<end:
    total = num[start]+num[end]
    if abs(answer)>=abs(total):
        answer = total
        result_start = start
        result_end = end

    if total == 0:
        break
    elif total < 0:
        start+=1
    else:
        end-=1

print(num[result_start],num[result_end])
