import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    result = {}

    for i in range(2,n+1):
        while n%i==0:
            if i not in result:
                result[i] = 1
            else:
                result[i]+=1
            n//=i

    for i,j in zip(result.keys(),result.values()):
        print(i,j)
