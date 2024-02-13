import sys

input = sys.stdin.readline

n = int(input())
em = list(map(int, input().split()))
graph = [[] for _ in range(n)]
child = [0]*n


for i in range(1, n):
    graph[em[i]].append(i)


def solution(x):
    if len(graph[x]) == 0:
        return
    child_cnt = []
    for i in graph[x]:
        solution(i)
        child_cnt.append(dp[i])

    if child_cnt:
        child_cnt.sort(reverse=True)
        parent = [child_cnt[i] + i+ 1 for i in range(len(child_cnt))]
        dp[x] = max(parent)


dp = [0]*n
solution(0)
print(dp[0])
