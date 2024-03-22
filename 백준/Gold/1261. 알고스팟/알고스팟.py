import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):
    q = deque()
    q.append([x, y])
    count[x][y] = 0

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < m and 0 <= ny < n:
                if count[nx][ny] == -1:
                    if board[nx][ny] == 1:
                        count[nx][ny] = count[a][b] + 1
                        q.append([nx, ny])
                    else:
                        count[nx][ny] = count[a][b]
                        q.appendleft([nx, ny])


count = [[-1] * n for _ in range(m)]
dfs(0, 0)
print(count[m-1][n-1])
