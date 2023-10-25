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

            if 0<=nx<n and 0<=ny<m and board[nx][ny]==1:
                board[nx][ny] = board[x][y]+1
                q.append([nx,ny])
                

    return board[n-1][m-1]
        

n,m = map(int,input().split())
board = [list(map(int,input().rstrip())) for _ in range(n)]
q=deque()

print(bfs(0,0))
