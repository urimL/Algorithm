import sys

input = sys.stdin.readline

# 거리가 k 이하인 햄버거 섭취 가능
# 햄버거 먹을 수 있는 사람의 최대 수

n, k = map(int, input().split())
hamburger = list(input().rstrip())

visited = [False] * n
for i in range(n):
    if hamburger[i] == "P":
        visited[i] = True

answer = 0

for i in range(n):
    if hamburger[i] == 'P':
        for j in range(i-k, i+k+1):
            if j < 0:
                continue
                
            if j == n:
                break

            if hamburger[j] == 'H' and not visited[j]:
                visited[j] = True
                answer += 1
                break

print(answer)