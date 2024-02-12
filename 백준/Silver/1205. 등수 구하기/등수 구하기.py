import sys

input = sys.stdin.readline


def solution():
    n, score, p = map(int, input().split())
    if n == 0:
        return 1

    scores = list(map(int, input().split()))
    if n == p and scores[-1] >= score:
        return -1

    else:
        cnt = n+1
        for i in range(n):
            if scores[i] <= score:
                cnt = i + 1
                break
        return cnt


print(solution())
