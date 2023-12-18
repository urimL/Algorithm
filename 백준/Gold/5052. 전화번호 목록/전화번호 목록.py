import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    answer = True
    n = int(input())
    number = []
    for i in range(n):
        number.append(input().rstrip())

    number.sort()

    for i in range(n-1):
        if number[i] == number[i+1][:len(number[i])]:
            answer = False
            break

    if answer:
        print('YES')
    else:
        print('NO')
