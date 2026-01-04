from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    q = deque()
    q.append((0, 0))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while q:
        x, y = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
        
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
                    
    return -1