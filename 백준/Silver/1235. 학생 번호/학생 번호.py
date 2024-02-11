import sys

input = sys.stdin.readline

n = int(input())
student = [input().rstrip() for _ in range(n)]
cnt = 1

while True:
    tmp = set()
    for s in student:
        tmp.add(s[-cnt:])
    if len(tmp) == n:
        break
    cnt+=1

print(cnt)