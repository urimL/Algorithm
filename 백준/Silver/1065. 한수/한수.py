import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    answer = 0

    for i in range(1, n + 1):
        ch = True
        tmp = str(i)
        if len(tmp) == 1:
            answer += 1
            continue
        d = int(tmp[0]) - int(tmp[1])
        for t in range(1, len(tmp) - 1):
            if int(tmp[t]) - int(tmp[t + 1]) != d:
                ch = False
                break

        if ch:
            answer += 1

    return answer


print(solution())
