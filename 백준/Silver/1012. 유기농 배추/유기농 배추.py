import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    q.append([x,y])

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<m and 0<=ny<n and board[nx][ny]==1:
                board[nx][ny] = 0
                q.append([nx,ny])         
        

t = int(input())

for i in range(t):
    count = 0
    q = deque()
    n,m,k = map(int,input().split())
    board = [[0]*n for _ in range(m)]
    for j in range(k):
        y,x = map(int,input().split())
        board[x][y]=1

    for r in range(m):
        for c in range(n):
            if board[r][c]==1:
                board[r][c]=0
                bfs(r,c)
                count+=1

    print(count)
