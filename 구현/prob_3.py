# 왕실의나이트 

# point: 나이트위치(C2)
# 열 : a ~ h, 행: 1 ~ 8
def test():
  point = input()
  column = list(point)[0]
  row = list(point)[1]

  columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
  rows = ['1', '2', '3', '4', '5', '6', '7', '8']

  # 총 8가지 위치 확인
  columnIndex = columns.index(column)
  rowIndex = rows.index(row)

  cases = [
    {'x':-1, 'y':-2},
    {'x':1, 'y':-2},
    {'x':1, 'y':2},
    {'x':-1, 'y':2},
    {'x':-2, 'y':-1},
    {'x':-2, 'y':1},
    {'x':2, 'y':-1},
    {'x':2, 'y':1},
  ]
  count = 0
  for case in cases:
    nr = rowIndex + case['x']
    nc = columnIndex + case['y']
    if (0 <= nr <= 7 and 0 <= nc <= 7):
      count += 1
  return count




# 답안예시
#
# def solution():
  

        