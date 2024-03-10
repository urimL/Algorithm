import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]

    score.sort()

    answer = 1
    max_score = score[0]
    for i in range(1, n):
        if score[i][1] < max_score[1]:
            max_score = score[i]
            answer += 1

    print(answer)
