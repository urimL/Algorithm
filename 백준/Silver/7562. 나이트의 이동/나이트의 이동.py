import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dx = [-2,-1,1,2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs():
    q = deque()
    chess[now[0]][now[1]]=1
    q.append([now[0],now[1]])

    while q:
        x,y = q.popleft()
        
        if [x,y]==target:
            return chess[x][y]-1
            
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<l and 0<=ny<l and chess[nx][ny]==0:
                chess[nx][ny]=chess[x][y]+1
                q.append([nx,ny])

        

for i in range(n):
    l = int(input())
    now = list(map(int,input().rstrip().split()))
    target = list(map(int,input().rstrip().split()))
    chess = [[0]*l for _ in range(l)]
    print(bfs())
