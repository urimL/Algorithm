from collections import deque

def solution(maps):
    answer = 0
    n,m = len(maps), len(maps[0])
    
    def bfs(x,y):
        
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        
        q = deque()
        q.append([x,y])
        
        while q:
            a,b = q.popleft()
            
            for i in range(4):
                nx = dx[i] + a
                ny = dy[i] + b
                
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                    q.append([nx,ny])
                    maps[nx][ny] = maps[a][b] + 1            
    
    bfs(0,0)
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]