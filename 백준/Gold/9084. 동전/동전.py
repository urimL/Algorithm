import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    total = int(input())

    d = [0] * (total + 1)
    d[0] = 1

    for coin in coins:
        for i in range(total + 1):
            if i >= coin:
                d[i] += d[i - coin]

    print(d[total])
