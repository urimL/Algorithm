# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            answer[i] = start
            dfs(i)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    answer = [0]*(n+1)

    for _ in range(1,n):
        s,e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    dfs(1)

    for i in range(2,n+1):
        print(answer[i])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
