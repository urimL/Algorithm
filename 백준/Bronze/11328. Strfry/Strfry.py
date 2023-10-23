import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a,b = map(str,input().split())
    a = "".join(sorted(a))
    b = "".join(sorted(b))

    if len(a)!=len(b):
        print('Impossible')
        continue

    for i in range(len(a)):
        if a[i]!=b[i]:
            check = False
            break
        else:
            check = True

    if check:
        print('Possible')
    else:
        print('Impossible')
