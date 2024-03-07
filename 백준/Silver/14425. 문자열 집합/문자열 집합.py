import sys

input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]
check = [input().rstrip() for _ in range(m)]

words = set(words)
inter = words.intersection(check)

answer = 0
for c in check:
    if c in inter:
        answer += 1
print(answer)
