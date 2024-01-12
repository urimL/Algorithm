import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
alp = list(input().split())
alp.sort()
alps = combinations(alp, n)


def check(a):
    v, c = 0, 0
    for i in a:
        if i in ["a", "e", "i", "o", "u"]:
            v += 1
        else:
            c += 1

    if v >= 1 and c >= 2:
        return True
    return False


for alp in alps:
    answer = ""
    if check(alp):
        for a in alp:
            answer += a
        print(answer)
