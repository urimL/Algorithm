from collections import deque

def bfs(a, b, graph):
    visited = [[0]*5 for _ in range(5)]
    visited[a][b] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    q = deque()
    q.append([a,b])
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y+ dy[i]
            
            if 0<=nx<5 and 0<=ny<5 and graph[nx][ny] == 'O':
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
            elif 0<=nx<5 and 0<=ny<5 and graph[nx][ny] == 'P':
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    return visited[nx][ny]-1

    return 3

def solution(places):
    answer = []
                                
    for p in places:
        graph = []
        check = True
        
        for i in range(5):
            graph.append(list(p[i]))
            
        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    if bfs(i,j,graph)<=2:
                        check = False
        
        if check:
            answer.append(1)
        else:
            answer.append(0)
                    
    
    return answer