n,m = map(int, input().split())
trees = list(map(int, input().split()))
answer = 0

def check(x):
    result = 0
    for t in trees:
        if t-x >= 0:
            result += (t-x)
    return result
    
start, end = 1, max(trees)
while start <= end:
    mid = (start + end)//2
    if check(mid) >= m:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)