from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    
    for r in roads:
        s,e = r
        graph[s].append(e)
        graph[e].append(s)
        
    def bfs(x):
        q = deque([x])
        visited = [False] * (n+1)
        visited[x] = True
        
        while q:
            now = q.popleft()
            
            for i in graph[now]:
                if not visited[i]:
                    cost[i] = min(cost[i], cost[now] + 1)   
                    q.append(i)
                    visited[i] = True
        
    
    cost = [500001] * (n+1)
    cost[destination] = 0
    bfs(destination)
    
    for s in sources:
        if cost[s] == 500001:
            answer.append(-1)
        else:
            answer.append(cost[s])
    
    return answer