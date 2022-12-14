# 시각 

# N: 시간 (0 ~ 23)
# 00시00분00초부터 N시59분59초까지 3이 하나라도 포함되는 모든 경우의 수를 출력
def test():

  print(list('923'))
  print(list(range(0, 60, 1)))
  
  N = int(input())

  firstCnt = 0
  secondCnt = 0
  totalCnt = 0
  # 분과 초는 고정이고 같으니까 하나만 계산해서 X 2
  for i in range(0, 60, 1):
    minutes = str(i)
    for j in range(0, 60, 1):
      seconds = str(j)
      data = f"{minutes}:{seconds}"
      if '3' in list(data):
        print('??' + data)
        firstCnt += 1
  # firstCnt *= firstCnt
  
  for i in range(0, N, 1):
    data = str(i)
    if '3' in list(data):
      print('@@' + data)
      secondCnt += 3600
    else:
      secondCnt += firstCnt
  totalCnt = firstCnt + secondCnt
  return totalCnt  


  # 4725


# 답안예시
#
def solution():
  h = int(input())
  count = 0
  for i in range(h + 1):
    for j in range(60):
      for k in range(60):
        if '3' in list(f"{i}{j}{k}"):
          count += 1
  return count

        