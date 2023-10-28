import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

com = combinations(arr,m)
for i in com:
    print(" ".join(map(str,i)))
