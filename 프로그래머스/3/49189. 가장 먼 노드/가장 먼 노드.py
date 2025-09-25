from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    q = deque([1])
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    
    for e,v in edge:
        graph[e].append(v)
        graph[v].append(e)
    
    while q:
        now = q.popleft()
        cnt = 1
        
        for x in graph[now]:
            if visited[x] == 0:
                visited[x] = visited[now] + 1
                q.append(x)
            
    max_value = max(visited)
    for i in range(1, n+1):
        if visited[i] == max_value:
            answer += 1
    
    
    return answer