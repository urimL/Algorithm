import sys
from itertools import combinations
input = sys.stdin.readline


while True:
    arr = list(map(int,input().split()))
    
    if len(arr)==1 and arr[0]==0:
        break

    comb = combinations(arr[1:],6)
    
    for i in comb:
        print(" ".join(list(map(str,i))))
    print()
    
