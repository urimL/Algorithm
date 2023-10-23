import math

def solution(a, b):
    denom = b//math.gcd(a,b)
    
    while denom>1:
        if denom%5==0:
            denom//=5
        elif denom%2==0:
            denom//=2
        else:
            return 2
    return 1