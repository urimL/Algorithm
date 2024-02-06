import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    children = []
    answer = 0
    for _ in range(n):
        children.append(int(input()))

    dp = [0] * n

    for i in range(n):
        for j in range(i):
            if children[i] > children[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    now = 0
    for i in dp:
        if i != now:
            answer += 1
        else:
            now += 1

    return answer


print(solution())
