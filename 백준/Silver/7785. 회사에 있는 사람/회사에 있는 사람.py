import sys

input = sys.stdin.readline

n = int(input())
em = {}
for i in range(n):
    a, b = map(str,input().split())

    if a not in em:
        em[a] = b
    elif a in em and em[a] =='enter':
        del em[a]

tmp = sorted(em.keys(), reverse=True)
for i in tmp:
    print(i)