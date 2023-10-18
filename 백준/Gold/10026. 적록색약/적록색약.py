from collections import deque

n = int(input())
a = [list(input()) for _ in range(n)]
q = deque()
visited = [[0]*n for _ in range(n)]

def bfs(x,y):
    q.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited[x][y] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n and a[nx][ny]==a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))


cnt1,cnt2 = 0,0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1+=1

for i in range(n):
    for j in range(n):
        if a[i][j]=="R":
            a[i][j] = "G"

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2+=1

print(cnt1,cnt2)
