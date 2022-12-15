# 현재상황에서 지금 당장 좋은것만 고르는 방법
# 거스름돈 문제
def test():

  charge = int(input())
  print(f"거스름돈 : {charge}")
  a = charge // 500
  b = (charge % 500) // 100
  c = (charge % 100) // 50
  d = (charge % 50) // 10
  return sum((a, b, c, d))


# 답안예시
def solution():
  charge = int(input())
  result = 0
  array = [500, 100, 50, 10]
  for i in array:
    result += charge // i
    charge %= i
  return result
