from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for s,e in roads:
        graph[s].append(e)
        graph[e].append(s)
        
    times = [500000001]*(n+1)
    times[destination] = 0
        
    def bfs(x):
        q = deque()
        q.append((x,0))
        visited = [False]*(n+1)
        visited[x] = True
        
        while q:
            now, cnt = q.popleft()

            for i in graph[now]:
                if not visited[i]:
                    if cnt+1 <= times[i]:
                        times[i] = cnt + 1
                        visited[i] = True
                        q.append((i,cnt+1))
    
    bfs(destination)
    for s in sources:
        if times[s] == 500000001:
            answer.append(-1)
        else:
            answer.append(times[s])
    return answer