def solution(park, routes):
    answer = []
    x,y = 0,0
    col,row = len(park),len(park[0])
    
    #start 지점 찾기
    for i in park:
        if "S" in i:
            x = i.find("S")
            break
        y+=1
          
    for route in routes:
        new_x = x
        new_y = y
        for r in range(int(route[2])):
            if route[0] == 'E' and new_x < len(park[0])-1 and park[new_y][new_x+1] != 'X':
                new_x += 1
                if r == int(route[2])-1:
                    x = new_x
            if route[0] == 'W' and new_x > 0 and park[new_y][new_x-1] != 'X':
                new_x -= 1
                if r == int(route[2])-1:
                    x = new_x
            if route[0] == 'N' and new_y > 0 and park[new_y-1][new_x] != 'X':
                new_y -= 1
                if r == int(route[2])-1:
                    y = new_y
            if route[0] == 'S' and new_y < len(park)-1 and park[new_y+1][new_x] != 'X':
                new_y += 1
                if r == int(route[2])-1:
                    y = new_y
                    
    return [y, x]
