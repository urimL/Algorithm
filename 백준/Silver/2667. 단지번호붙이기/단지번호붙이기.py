import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append([x,y])
    total = 1

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n and board[nx][ny]==1:
                board[nx][ny]=0
                total+=1
                q.append([nx,ny])
                
    return total

n = int(input())
board = [list(map(int,input().rstrip())) for _ in range(n)]
count = 0
houses = []
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            count+=1
            board[i][j]=0
            houses.append(bfs(i,j))

houses.sort()
print(count)
for i in houses:
    print(i)
