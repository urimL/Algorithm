from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
distance = [[0] *m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()

def bfs(Dx,Dy):
    while q:
        x,y = q.popleft()
        if graph[Dx][Dy] == 'S':
            return distance[Dx][Dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx,ny))
                elif (graph[nx][ny] =='.' or graph[nx][ny] =='S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    q.append((nx,ny))
    return "KAKTUS"


for x in range(n):
    for y in range(m):
        if graph[x][y] == 'S':
            q.append((x,y))
        elif graph[x][y] == 'D':
            Dx,Dy = x,y

for x in range(n):
    for y in range(m):
        if graph[x][y] == '*':
            q.append((x,y))

print(bfs(Dx,Dy))