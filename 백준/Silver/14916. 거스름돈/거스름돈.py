import sys

input = sys.stdin.readline
n = int(input())
answer = 0
five = n // 5

while n > 0:
    if five < 0:
        answer = -1
        break
    tmp = n - five * 5
    if tmp % 2 == 0:
        answer += five + tmp // 2
        break
    else:
        five -= 1
        continue

print(answer)
