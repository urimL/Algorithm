import sys

input = sys.stdin.readline

n = int(input())
s = [list(input().rstrip()) for _ in range(n)]
words = dict()

for i in s:
    x = len(i) - 1
    for j in i:
        if j in words:
            words[j] += 10**x
        else:
            words[j] = 10**x
        x -= 1

words = sorted(words.values(), reverse=True)
answer, now = 0, 9
for w in words:
    answer += w * now
    now -= 1

print(answer)
