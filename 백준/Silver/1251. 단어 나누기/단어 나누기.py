import sys

input = sys.stdin.readline

word = list(input().rstrip())
result = []

for i in range(1, len(word)-1):
    tmp = []
    for j in range(i+1, len(word)):
        tmp = ((word[0:i:])[::-1]) + ((word[i:j:])[::-1]) + ((word[j::])[::-1])
        result.append(tmp)

result.sort()
print("".join(result[0]))