import sys

input = sys.stdin.readline

m, n = map(int, input().split())
dic = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
       '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}
result = []

for i in range(m, n + 1):
    a = ' '.join([dic[j] for j in str(i)])
    result.append([i, a])

result.sort(key=lambda x: x[1])

for i in range(len(result)):
    if i % 10 == 0 and i != 0:
        print(sep="\n")
    print(result[i][0], end=" ")