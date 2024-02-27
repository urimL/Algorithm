import sys

input = sys.stdin.readline

n = int(input())
tips = [int(input()) for _ in range(n)]
answer = 0

tips.sort(reverse=True)
for i in range(n):
    tip = tips[i] - i
    if tip > 0:
        answer += tip

print(answer)
