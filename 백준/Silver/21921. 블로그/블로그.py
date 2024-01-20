import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visitants = list(map(int, input().split()))

if max(visitants) == 0:
    print("SAD")

else:
    window = sum(visitants[:x])
    answer = window
    cnt = 1

    for i in range(x, n):
        window += visitants[i] - visitants[i-x]
        if window > answer:
            cnt = 1
            answer = window
        elif window == answer:
            cnt += 1
    print(answer)
    print(cnt)
    