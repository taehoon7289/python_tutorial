# 미로 탈출

# 두정수 n, m 은 행, 열
# 1,1 부터 출구 N,M 까지 최소거리

from collections import deque

# global n, m
n, m = map(int, input().split())

graph = []
# result = 0
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
  # global n, m
  queue = deque()
  queue.append((x, y))
  while queue:
    print("queue", queue)
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  print(graph)
  return graph[n - 1][m - 1]


print(bfs(0, 0))
