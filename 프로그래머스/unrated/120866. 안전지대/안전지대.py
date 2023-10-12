def solution(board):
    answer = 0
    
    n=len(board)
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]
    
    point = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==1:
                point.append((i,j))
    
    for x,y in point:
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                board[nx][ny] = 1
    
    for x in range(n):
        for y in range(n):
            if board[x][y]==0:
                answer+=1
    return answer