def solution(lines):
    answer=0
    point=[0]*200
    
    for i in range(len(lines)):
        for j in range(lines[i][0],lines[i][1]):
            point[j+100]+=1
            
    answer+=point.count(2)
    answer+=point.count(3)
    
    return answer