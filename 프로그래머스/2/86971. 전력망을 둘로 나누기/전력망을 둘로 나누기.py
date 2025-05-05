from collections import deque

def solution(n, wires):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for s,e in wires:
        graph[s].append(e)
        graph[e].append(s)
        
    def bfs(start):
        visited = [False] * (n+1)
        q = deque([start])
        visited[start] = True
        cnt = 1
        
        while q:
            now = q.popleft()
            for x in graph[now]:
                if not visited[x]:
                    q.append(x)
                    visited[x] = True
                    cnt += 1
        return cnt
    
    answer = n
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(abs(bfs(a)-bfs(b)), answer)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer