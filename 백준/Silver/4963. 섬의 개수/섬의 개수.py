import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append([nx, ny])


while True:
    answer = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                answer += 1
                bfs(i, j)

    print(answer)
