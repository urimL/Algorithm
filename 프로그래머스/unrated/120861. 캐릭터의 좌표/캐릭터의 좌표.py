def solution(keyinput, board):
    x,y = 0,0
    max_x,min_x = board[0]//2,-(board[0]//2)
    max_y,min_y = board[1]//2,-(board[1]//2)
    
    for i in keyinput:
        if i=="left" and x-1>=min_x:
            x-=1
        elif i=="down" and y-1>=min_y:
            y-=1
        elif i=="right" and x+1<=max_x:
            x+=1
        elif i=="up" and y+1<=max_y:
            y+=1
    
    return [x,y]