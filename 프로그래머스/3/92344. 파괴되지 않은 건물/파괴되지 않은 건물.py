def solution(board, skill):
    answer = 0
    tmp = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    
    for s in skill:
        t, x1, y1, x2, y2, w = s
        tmp[x1][y1] += w if t == 2 else -w
        tmp[x1][y2+1] += -w if t==2 else w
        tmp[x2+1][y1] += -w if t==2 else w
        tmp[x2+1][y2+1] += w if t==2 else -w
        
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i][j+1] += tmp[i][j]
            
    for j in range(len(tmp[0])-1):
        for i in range(len(tmp)-1):
            tmp[i+1][j] += tmp[i][j]
            
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]
            if board[i][j] >= 1:
                answer += 1
 
    return answer