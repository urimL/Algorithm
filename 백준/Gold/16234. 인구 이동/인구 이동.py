import sys
from collections import deque

input = sys.stdin.readline

n, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    path = [[x, y]]

    while q:
        a, b = q.popleft()

        for r in range(4):
            nx = dx[r] + a
            ny = dy[r] + b

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if L <= abs(board[nx][ny] - board[a][b]) <= R:
                    path.append([nx, ny])
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return path


answer = 0
while True:
    visited = [[False] * (n+1) for _ in range(n+1)]
    fin = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                country = bfs(i, j)

                if len(country) > 1:
                    fin = True
                    total = sum([board[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        board[x][y] = total
    if not fin:
        break
    answer += 1

print(answer)
