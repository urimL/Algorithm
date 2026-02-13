from collections import deque
import sys

input = sys.stdin.readline

n,m,h = map(int, input().split())

box = []
q = deque()
answer = 0

for z in range(h):
    layer = []
    for y in range(m):
        row = list(map(int, input().split()))
        layer.append(row)
        for x in range(n):
            if row[x] == 1:
                q.append((z, y, x))
    box.append(layer)
    
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while q:
    z, y, x = q.popleft()

    for i in range(6):
        nx = dx[i] + x
        ny = dy[i] + y
        nz = dz[i] + z

        if 0<=nx<n and 0<=ny<m and 0<=nz<h:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                q.append((nz,ny,nx))

for z in range(h):
    for y in range(m):
        for x in range(n):
            if box[z][y][x] == 0:
                print(-1)
                exit()
            answer = max(answer, box[z][y][x])

print(answer-1)