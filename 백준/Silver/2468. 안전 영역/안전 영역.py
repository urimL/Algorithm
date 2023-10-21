import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = -1

def dfs(x,y,h):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if (0<=nx<n) and (0<=ny<n) and not visited[nx][ny] and board[nx][ny]>h:
            visited[nx][ny]=1
            dfs(nx,ny,h)


n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

for k in range(max(map(max,board))):
    visited = [[0]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j]>k and not visited[i][j]:
                count+=1
                visited[i][j]=1
                dfs(i,j,k)
    ans = max(ans,count)

print(ans)
