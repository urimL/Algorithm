import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
like = dict()

for _ in range(k):
    st = input().rstrip()
    like[st] = 0


def bfs(i, j):
    q = deque()
    q.append((i, j, board[i][j]))

    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]

    while q:
        x, y, now_st = q.popleft()

        if now_st in like:
            like[now_st] += 1

        if len(now_st) >= 5:
            continue

        for r in range(8):
            nx = dx[r] + x
            ny = dy[r] + y

            if nx == -1:
                nx = n - 1
            elif nx == n:
                nx = 0

            if ny == -1:
                ny = m - 1
            elif ny == m:
                ny = 0
            q.append((nx, ny, now_st + board[nx][ny]))


for i in range(n):
    for j in range(m):
        bfs(i, j)

for k in like.keys():
    print(like[k])
