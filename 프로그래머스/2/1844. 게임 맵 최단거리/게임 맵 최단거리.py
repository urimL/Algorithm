from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # ✅ 행, 열 순서로 선언!
    q = deque()
    q.append((0, 0))
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True

    # 이동 방향: 하, 우, 상, 좌
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        y, x = q.popleft()

        if y == n-1 and x == m-1:
            return maps[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    maps[ny][nx] = maps[y][x] + 1
                    q.append((ny, nx))

    return -1  # 도달 불가능
