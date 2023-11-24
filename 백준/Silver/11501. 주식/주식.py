import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    max_value,answer = 0,0

    for i in range(n-1,-1,-1):
        if l[i]>max_value:
            max_value = l[i]
        else:
            answer+=max_value-l[i]
    print(answer)