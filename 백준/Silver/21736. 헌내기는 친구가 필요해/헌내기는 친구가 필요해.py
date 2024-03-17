import sys
from collections import deque
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    global answer

    while q:
        now = q.popleft()

        for i in range(4):
            nx = dx[i] + now[0]
            ny = dy[i] + now[1]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:

                if board[nx][ny] == "X":
                    visited[nx][ny] = True
                    continue

                if board[nx][ny] == "P":
                    answer += 1
                visited[nx][ny] = True
                q.append([nx, ny])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * m for _ in range(n)]
answer = 0
for a in range(n):
    for b in range(m):
        if board[a][b] == "I":
            visited[a][b] = True
            bfs(a, b)

if answer == 0:
    print("TT")
else:
    print(answer)
