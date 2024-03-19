import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]


def dfs(x, y):
    visited[x][y] = True
    if board[x][y] == "-":
        nx, ny = x, y + 1
        if 0 < ny < m and board[nx][ny] == "-" and not visited[nx][ny]:
            dfs(nx, ny)

    else:
        nx, ny = x + 1, y
        if 0 < nx < n and board[nx][ny] == "|" and not visited[nx][ny]:
            dfs(nx, ny)


answer = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            answer += 1
print(answer)
