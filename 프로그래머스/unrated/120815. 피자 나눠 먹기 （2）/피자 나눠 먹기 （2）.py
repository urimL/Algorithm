import math
def solution(n):
    answer = 0
    
    #n과 6의 최소공배수에서 6을 나눔
    answer = n*6//math.gcd(n,6)//6
    
    return answer