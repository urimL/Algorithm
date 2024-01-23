from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    count = [-1]*(n+1)
    
    for i in edge:
        v,e = i
        graph[v].append(e)
        graph[e].append(v)
        
    q = deque([1])
    count[1] = 0
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if count[i] == -1:
                q.append(i)
                count[i] = count[now]+1
    
    answer = count.count(max(count))
        
    return answer