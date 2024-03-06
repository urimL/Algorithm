import sys

input = sys.stdin.readline

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
result = dict()

p.sort(key=lambda x: x[2], reverse=True)

cnt = 0
for i in p:
    if i[0] in result:
        if len(result[i[0]]) < 2:
            result[i[0]].append(i[1])
            cnt += 1
    else:
        result[i[0]] = [i[1]]
        cnt += 1

    if cnt == 3:
        break

for r in result:
    for i in result[r]:
        print(r, i)
