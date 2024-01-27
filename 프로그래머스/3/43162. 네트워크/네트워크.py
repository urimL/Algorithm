from collections import deque

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False]*n
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    
    def bfs(x):
        q = deque([x])
        
        while q:
            now = q.popleft()
            visited[now] = True
            
            for X in graph[now]:
                if not visited[X]:
                    q.append(X)
                    visited[X] = True
               
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer+=1
        
    return answer