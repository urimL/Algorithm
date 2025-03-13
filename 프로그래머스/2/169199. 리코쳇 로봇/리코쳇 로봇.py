from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(board):
    answer = 0
    n,m = len(board), len(board[0])
    count = [[999999999]*m for _ in range(n)]
    
    def bfs(a,b):
        q = deque()
        q.append([a,b,0])
        visited = [[False]*m for _ in range(n)]
        
        while q:
            x,y,c = q.popleft()
            
            if board[x][y] == 'G':
                return c
            
            for i in range(4):
                nx, ny = x,y
                while 0<=nx+dx[i]<n and 0<=ny+dy[i]<m and board[nx+dx[i]][ny+dy[i]] != 'D':
                    nx += dx[i]
                    ny += dy[i]
                    
                if count[nx][ny] > c+1:
                    count[nx][ny] = c+1
                    q.append([nx,ny,c+1])
        return -1   
                    
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                answer = bfs(i,j)
                
    return answer