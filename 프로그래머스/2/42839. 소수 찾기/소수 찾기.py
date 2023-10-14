import math
from itertools import permutations

def solution(numbers):
    answer = 0
    result = []
    
    #소수찾기
    def is_prime_num(n):
        if n==1:
            return False
        for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
            if n % i == 0:
                return False
        return True
    
    #소수인 조합 result에 저장
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            tmp = "".join(p)
            if is_prime_num(int(tmp)) and tmp not in result and tmp.startswith('0')==0:
                result.append(tmp)
                answer+=1
        
    print(result)
    return answer