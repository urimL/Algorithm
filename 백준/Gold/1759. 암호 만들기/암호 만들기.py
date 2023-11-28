import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(input().split())
a.sort()
answer = []


def check(cnt,idx):
    if cnt == n:
        v, c = 0, 0
        for i in range(n):
            if answer[i] in ["a", "e", "i", "o", "u"]:
                v += 1
            else:
                c += 1
        if v >= 1 and c >= 2:
            print("".join(answer))
        return

    for i in range(idx,m):
        answer.append(a[i])
        check(cnt+1,i+1)
        answer.pop()


check(0,0)