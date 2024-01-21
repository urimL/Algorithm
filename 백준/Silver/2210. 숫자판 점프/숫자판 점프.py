import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(x, y, result):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if len(result) == 6:
        if result not in answer:
            answer.append(result)
        return

    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, result+board[nx][ny])


board = [list(input().rstrip().split()) for _ in range(5)]
answer = []
for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(answer))
