# 음료수 얼려 먹기

# 첫번째줄에 얼음틀의 세로 길이 N, 가로길이 M이 주어진다
# 이때 구멍이 뚫려 있는 부분은 0, 그렇지 않은 부분은 1
# 한번에 만들수 있는 아이스크림 개수 출력

# 답안예시
#


def dfs(r, c):
  print("인자값 : ", r, c)
  if r < 0 or r >= n or c < 0 or c >= m:
    return False

  if graph[r][c] == 0:
    graph[r][c] = 1
    dfs(r - 1, c)
    dfs(r + 1, c)
    dfs(r, c - 1)
    dfs(r, c + 1)
    return True
  return False


n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

result = 0

for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 진행
    if dfs(i, j) == True:
      result += 1

print("result", result)
