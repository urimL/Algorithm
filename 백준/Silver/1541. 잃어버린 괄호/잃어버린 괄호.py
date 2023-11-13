import sys
input = sys.stdin.readline

s = list(input().rstrip().split('-'))
answer = 0

for i in range(len(s)):
    total = 0
    tmp = list(s[i].split('+'))

    for t in tmp:
        total += int(t)

    if i==0:
        answer+=total
    else:
        answer-=total

print(answer)
