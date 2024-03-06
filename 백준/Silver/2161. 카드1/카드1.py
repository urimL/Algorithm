import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = deque([i for i in range(1, n + 1)])
away = []
last = 0

while cards:
    if len(cards) > 1:
        away.append(cards.popleft())
        if cards:
            cards.append(cards.popleft())
            last = cards[0]
    else:
        last = cards[0]
        break

print(*away, last)
