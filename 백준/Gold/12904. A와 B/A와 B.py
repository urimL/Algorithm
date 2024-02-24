import sys

input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())
tmp = t
check = False

for i in range(len(t) - 1, -1, -1):
    if tmp == s:
        check = True
        break
    if t[i] == "A":
        tmp.pop()
    elif t[i] == "B":
        tmp.pop()
        tmp.reverse()

if check:
    print(1)
else:
    print(0)
