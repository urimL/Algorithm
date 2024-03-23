import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    while coins:
        tmp1, tmp2, cnt = coins.popleft()
        a, b = tmp1
        c, d = tmp2

        if cnt >= 10:
            return -1

        for r in range(4):
            na, nb = dx[r] + a, dy[r] + b
            nc, nd = dx[r] + c, dy[r] + d
            t = []

            if 0 <= na < n and 0 <= nb < m and 0 <= nc < n and 0 <= nd < m:
                if board[na][nb] == "#":
                    na, nb = a, b

                if board[nc][nd] == "#":
                    nc, nd = c, d

                t.append([na, nb])
                t.append([nc, nd])
                t.append(cnt + 1)
                coins.append(t)

            elif 0 <= na < n and 0 <= nb < m:
                return cnt + 1
            elif 0 <= nc < n and 0 <= nd < m:
                return cnt + 1
            else:
                continue
    return -1


answer = 0
coins = deque()
tmp = []
for i in range(n):
    for j in range(m):
        if board[i][j] == "o":
            tmp.append([i, j])
tmp.append(0)
coins.append(tmp)
print(bfs())
