import sys

input = sys.stdin.readline

n,m = map(int,input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = list(a-b)
result.sort()

if len(result) == 0:
    print(0)

else:
    print(len(result))
    print(*result)
