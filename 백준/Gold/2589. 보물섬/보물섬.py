from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int,input().split())
board = []
answer = 0

for _ in range(n):
    board.append(input().rstrip())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append([x,y])
    cnt = 0

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]

            if 0>nx or nx>=n or 0>ny or ny>=m:
                continue
            elif visited[nx][ny] == 0 and board[nx][ny] == 'L':
                visited[nx][ny] = visited[a][b] + 1
                cnt = max(cnt, visited[nx][ny])
                q.append([nx,ny])
    return cnt-1


for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            answer = max(answer, bfs(i,j))

print(answer)

