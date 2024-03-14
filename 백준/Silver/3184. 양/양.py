import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
back = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]


def bfs(a, b):
    count = [0, 0]
    q = deque()
    q.append([a, b])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if back[nx][ny] == "#":
                    continue
                if back[nx][ny] == "v":
                    count[1] += 1
                elif back[nx][ny] == "o":
                    count[0] += 1

                visited[nx][ny] = True
                q.append([nx, ny])

    return count


answer = [0, 0]
for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            visited[i][j] = True
            result = bfs(i, j)

            if result[0] > result[1]:
                answer[0] += result[0]
            else:
                answer[1] += result[1]

print(*answer)
