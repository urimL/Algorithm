import sys
input = sys.stdin.readline

n,k = map(int,input().split())
pos = 0
arr = [i for i in range(1,n+1)]
answer = []

for i in range(n):
    pos+=k-1
    if pos>=len(arr):
        pos%=len(arr)
    answer.append(str(arr.pop(pos)))

print("<",', '.join(answer),">",sep="")
