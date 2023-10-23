def solution(dots):
    answer = 0
    x_dots,y_dots = [],[]
    
    for i in dots:
        x_dots.append(i[0])
        y_dots.append(i[1])
    
    answer = (max(x_dots)-min(x_dots))*(max(y_dots)-min(y_dots))
    
    return answer