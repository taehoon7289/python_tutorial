# 미로 탈출

# 두정수 n, m 은 행, 열
# 1,1 부터 출구 N,M 까지 최소거리

from collections import deque

n, m = map(int, input().split())

graph = []
# result = 0
for i in range(n):
  graph.append(list(map(int, input())))

# print(graph)

queue = deque()


def check(row, col):
  if row < 0 or row >= n or col < 0 or col >= m:
    return False
  if graph[row][col] == 1:
    graph[row][col] = 0
    return True
  return False


keepGoingFlag = True
pathCnt = 0


def bfs(row, col, result):
  if row == n - 1 and col == m - 1:
    global pathCnt, keepGoingFlag
    pathCnt = result
    keepGoingFlag = False
  else:
    # 인접노드 찾기
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for d in directions:
      # queue 에 삽입
      if check(row + d[0], col + d[1]) == True:
        global queue
        queue.append([row + d[0], col + d[1], result + 1])
    # queue 뽑으면서
    if keepGoingFlag == True and len(queue) > 0:
      point = queue.popleft()
      bfs(point[0], point[1], point[2])


bfs(0, 0, 1)
print(pathCnt)
