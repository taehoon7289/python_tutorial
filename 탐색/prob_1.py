# 음료수 얼려 먹기

# 첫번째줄에 얼음틀의 세로 길이 N, 가로길이 M이 주어진다
# 이때 구멍이 뚫려 있는 부분은 0, 그렇지 않은 부분은 1
# 한번에 만들수 있는 아이스크림 개수 출력
import sys


def test():

  readArray = list(map(int, sys.stdin.readline().split()))
  global row, column, array
  row, column = readArray[0], readArray[1]
  array = []
  for j in range(row):
    columnArray = list(sys.stdin.readline())
    array.append(list(map(int, columnArray[0:len(columnArray) - 1])))
  # print(len(array))
  # print(len(array[0]))

  global ri, ci
  ri, ci = 0, 0
  global groupCnt
  groupCnt = 0
  global visited
  visited = [[False for i in array[j]] for j in range(len(array))]
  # print(visited)
  global directionList
  directionList = [[-1, 0], [1, 0], [0, -1], [0, 1]]

  def dfsFn(ri, ci):
    global visited, array, groupCnt, directionList
    if array[ri][ci] == 0 and visited[ri][ci] == False:
      visited[ri][ci] = True
      # 인접노드확인 상하좌우
      for direction in directionList:
        visitedFn(ri, ci, direction)
      # print("ri ci", ri, ci)
      groupCnt += 1
    # else:
    # print("안됨")

  def visitedFn(ri, ci, direction):
    global array, visited, row, column, directionList
    nr = ri + direction[0]
    nc = ci + direction[1]
    # print("row, column", row, column)
    if 0 <= nr <= row - 1 and 0 <= nc <= column - 1:
      # print("nr, nc", nr, nc)
      if array[nr][nc] == 0 and visited[nr][nc] == False:
        visited[nr][nc] = True
        # print("True 변경@@@@@@@@")

        for direction in directionList:
          visitedFn(nr, nc, direction)

  for r in range(len(array)):
    for c in range(len(array[r])):
      # 시작
      dfsFn(r, c)
  # print(visited)
  return groupCnt


# 답안예시
#
# def solution():
