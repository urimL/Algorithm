import sys
from itertools import product
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

tmp = []

def dfs():
    if len(tmp)==m:
            print(" ".join(map(str,tmp)))
            return
        
    for i in arr:
        if not tmp or tmp[-1]<=i:
            tmp.append(i)
            dfs()
            tmp.pop()

dfs()
