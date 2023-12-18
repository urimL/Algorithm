import sys

input = sys.stdin.readline

n, m = map(int,input().split())
ear, eye = [],[]

for i in range(n):
    ear.append(input().rstrip())

for i in range(m):
    eye.append(input().rstrip())

answer = list(set(eye) & set(ear))
answer.sort()

print(len(answer))
for i in answer:
    print(i)