def solution(hp):
    answer = 0
    
    if hp>=5:
        answer+=hp//5
        hp%=5

    if hp>=3:
        answer+=hp//3
        hp%=3

    if 1<=hp<3:
        answer+=hp
    
    return answer