def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]
    
    for i,j in results:
        board[i-1][j-1] = 1
        board[j-1][i-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][k] == 1 and board[k][j] == 1:
                    board[i][j] = 1
                    board[j][i] = -1
                if board[i][k] == -1 and board[k][j] == -1:
                    board[i][j] = -1

    for i in range(n):
        cnt = board[i].count(0)
        
        if cnt == 1:
            answer+=1

    return answer