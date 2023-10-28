import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]

comb = combinations(arr,m)
for x in comb:
    print(" ".join(map(str,x)))
