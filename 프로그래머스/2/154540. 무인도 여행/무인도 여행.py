from collections import deque

def solution(maps):
    answer = []
    
    def bfs(a,b):       
        count = int(maps[a][b])
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        q = deque()
        q.append([a,b])
        visited[a][b] = True
        
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                    count += int(maps[nx][ny])
                    visited[nx][ny] = True
                    q.append([nx,ny])
        
        return count
        
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i,j))
    
    answer.sort()
    if not answer:
        return [-1]
    
    return answer