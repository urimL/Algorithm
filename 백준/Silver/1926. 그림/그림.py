import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
painting = [list(map(int,input().split())) for i in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    painting[x][y]=0
    w = 1
    q = [[x,y]]

    while q:
        x,y = q.pop()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and painting[nx][ny]==1:
                q.append([nx,ny])
                painting[nx][ny]=0
                w+=1
    return w
            

cnt = 0
answer = 0
for i in range(n):
    for j in range(m):
        if painting[i][j]==1:
            cnt += 1
            answer = max(dfs(i,j),answer)

print(cnt)
print(answer)
            
