from collections import deque

def solution(info, edges):
    answer = []
    visited = [False] * len(info)
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for s,e in edges:
            if visited[s] and not visited[e]:
                visited[e] = True
                
                if info[e] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[e] = False
                
    visited[0] = True
    dfs(1,0)
    
    return max(answer)