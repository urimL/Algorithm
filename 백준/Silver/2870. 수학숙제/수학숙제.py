import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
result = []

for i in range(n):
    st = input().rstrip()
    tmp = ''

    for s in st:
        if '0'<=s<='9':
            tmp += s
        else:
            if tmp != '':
                result.append(int(tmp))
            tmp = ''

    if tmp != '':
        result.append(int(tmp))

result.sort()
print(*result, sep = '\n')