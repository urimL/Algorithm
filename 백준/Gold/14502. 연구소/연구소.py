import sys
from collections import deque
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    global answer
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    tmp = copy.deepcopy(board)

    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append([i, j])

    while q:
        x, y = q.popleft()

        for r in range(4):
            nx = dx[r] + x
            ny = dy[r] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append([nx, ny])

    cnt = 0
    for r in range(n):
        cnt += tmp[r].count(0)

    answer = max(answer, cnt)


def build(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                build(cnt + 1)
                board[i][j] = 0


answer = 0
build(0)
print(answer)
