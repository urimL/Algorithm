import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a,b = map(str,input().split())
    a,b = list(a),list(b)
    visited = [False]*len(a)
    check = False

    if len(a)!=len(b):
        print('Impossible')
        continue

    for j in range(len(a)):
        if a[j] not in b:
            print('Impossible')
            check = False
            break
        elif a[j] in b and not visited[j]:
            visited[j]=True
            b.remove(a[j])
            check = True
        else:
            print('Impossible')
            check = False
            break

    if check:
        print('Possible')
