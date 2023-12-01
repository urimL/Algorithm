import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,k = map(int,input().split())
food = []
visited = [[True]*m for _ in range(n)]
answer = []


def dfs(x,y):
    global count
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = True

    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            count+=1
            visited[nx][ny] = True
            dfs(nx,ny)
    return count


for _ in range(k):
    x,y = map(int,input().split())
    food.append([x-1,y-1])
    visited[x-1][y-1] = False

for i in food:
    if not visited[i[0]][i[1]]:
        count = 1
        answer.append(dfs(i[0],i[1]))

print(max(answer))
