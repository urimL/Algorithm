import sys

input = sys.stdin.readline

n = int(input())
answer = 0


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


num = factorial(n)

while num > 1:
    if num % 10 == 0:
        answer += 1
        num //= 10
    else:
        break

print(answer)
