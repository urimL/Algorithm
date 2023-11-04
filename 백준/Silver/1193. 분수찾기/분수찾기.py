import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
cnt,line = 0,0
result = []

while cnt<x:
    line+=1
    cnt+=line

pos = cnt-line

for i in range(1,x-pos+1):
    if line%2==0:
        result.append([i,line+1-i])
    else:
        result.append([line+1-i,i])

print(result[-1][0],'/',result[-1][1],sep='')
