from collections import deque
    
def solution(land):    
    r, c = len(land), len(land[0])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    def bfs(a,b):
        column = set()
        q = deque()
        q.append([a,b])
        visited[a][b] = True
        column.add(b)

        cnt = 0
        
        while q:
            x,y = q.popleft()
            cnt += 1
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and land[nx][ny] == 1:
                    q.append([nx,ny])
                    visited[nx][ny] = True
                    column.add(ny)
        
        result = [list(column), cnt]
        return result
                
                
    answer = 0
    visited = [[False]*(c) for _ in range(r)]
    result = []
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and land[i][j] == 1:
                t = bfs(i,j)
                result.append(t)
                
    answer = [0] * c
    for r in result:
        for k in r[0]:
            answer[k] += r[1]
    
    return max(answer)