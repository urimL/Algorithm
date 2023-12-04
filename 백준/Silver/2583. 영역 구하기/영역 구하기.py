import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
visited = [[False] * m for _ in range(n)]
answer = []
total = 0


def coloring(x1, y1, x2, y2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = True


def dfs(x, y,count):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = True

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            count = dfs(nx, ny, count+1)
    return count


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    coloring(x1, y1, x2, y2)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            count = 1
            answer.append(dfs(i, j, count))
            total += 1

print(len(answer))
answer.sort()
for num in answer:
    print(num,end=' ')
