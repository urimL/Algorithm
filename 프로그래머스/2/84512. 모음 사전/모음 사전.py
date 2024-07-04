from itertools import product

def solution(word):
    answer = 0
    total = set()
    alphabet = ['A','E','I','O','U','']
    
    prod = product(alphabet, repeat = 5)
    
    for p in prod:
        tmp = "".join(list(p))
        total.add(tmp)
        
    total = list(total)
    total.sort()
    
    for t in total:
        if t == word:
            return answer
        answer += 1
