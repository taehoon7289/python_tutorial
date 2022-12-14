# 상하좌우 

# N: 공간의 크기 n X n , 다음 data: 이동할 계획서

def test():
  N = int(input())
  data = list(input().split())
  # x: 열, y: 행
  result = {'x': 0, 'y': 0}

  for s in data:
    if s == 'L':
      result = left(result) 
    elif s == 'R':
      result = right(N, result)
    elif s == 'U':
      result = up(result)
    else:
      result = down(N, result)
  result['x'] += 1
  result['y'] += 1
  return str(result["y"]) + " " + str(result["x"])
  


def left(result):
  if result['x'] != 0:
    result['x'] -= 1
  return result

def right(N, result):
  if result['x'] != N-1:
    result['x'] += 1
  return result

def up(result):
  if result['y'] != 0:
    result['y'] -= 1
  return result

def down(N, result):
  if result['y'] != N-1:
    result['y'] += 1
  return result
  


# 답안예시
#
def solution():
  N = int(input())
  plans = input().split()

  x, y = 1, 1
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  move_type = ['L', 'R', 'U', 'D']

  for plan in plans:
    for index in range(len(move_type)):
      if plan == move_type[index]:
        nx = x + dx[index]
        ny = y + dy[index]
        # print("nx , ny", nx , ny)

    if 0 < nx < N and 0 < ny < N:
        x,y = nx, ny
  return f"{x} {y}"      
        