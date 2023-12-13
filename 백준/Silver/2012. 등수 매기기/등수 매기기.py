import sys

input = sys.stdin.readline

n = int(input())
score = []
pos = 1
answer = 0

for _ in range(n):
    score.append(int(input()))

score.sort()

for i in score:
    answer+=abs(pos-i)
    pos+=1

print(answer)