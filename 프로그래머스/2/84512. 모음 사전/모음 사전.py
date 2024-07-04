from itertools import product

def solution(word):
    total = set()
    alphabet = ['A','E','I','O','U','']
    
    prod = product(alphabet, repeat = 5)
    
    for p in prod:
        tmp = "".join(list(p))
        total.add(tmp)
        
    total = list(total)
    total.sort()
    
    idx = total.index(word)
    return idx