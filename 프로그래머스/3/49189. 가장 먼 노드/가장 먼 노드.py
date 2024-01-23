from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    count = [0]*(n+1)
    
    for i in edge:
        v,e = i
        graph[v].append(e)
        graph[e].append(v)
        
    def bfs(x):
        q = deque([x])
        
        while q:
            now = q.popleft()
            if not visited[now]:
                visited[now] = True
                for i in graph[now]:
                    if not visited[i]:
                        q.append(i)
                        if count[i]==0:
                            count[i] = count[now]+1
                        else:
                            count[i] = min(count[i],count[now]+1)
                                           
    visited = [False]*(n+1)
    bfs(1)
    answer = count.count(max(count))
        
    return answer