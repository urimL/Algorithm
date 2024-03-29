from collections import deque

def solution(maps):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    
    def bfs(x,y):
        q = deque()
        q.append([x,y])
        
        while q:
            a, b = q.popleft()
            
            for i in range(4):
                nx = dx[i] + a
                ny = dy[i] + b
                
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[a][b]+1
                    q.append([nx,ny])

    bfs(0,0)
    if maps[len(maps)-1][len(maps[0])-1] == 1:
        return -1
    else:
        return maps[len(maps)-1][len(maps[0])-1]
                    
        