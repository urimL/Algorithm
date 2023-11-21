import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    
    def dfs(now,count):
        visited[now] = True
        for i in graph[now]:
            if not visited[i]:
                count = dfs(i,count+1)
        return count   

    for _ in range(t):
        n,m = map(int,input().split())
        graph = [[] for i in range(n+1)]
        visited = [False]*(n+1)
        answer = 0

        for i in range(m):
            s,e = map(int,input().split())
            graph[s].append(e)
            graph[e].append(s)

        print(dfs(1,0))

if __name__ == '__main__':
    solution()
