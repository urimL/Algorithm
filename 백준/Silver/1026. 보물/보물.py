import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0

tmp = []
for i in range(len(b)):
    tmp.append([i, b[i]])

tmp.sort(key = lambda x:x[1])
a.sort(reverse = True)

for i in range(len(a)):
    answer += tmp[i][1] * a[i]

print(answer)
    
