# 현재상황에서 지금 당장 좋은것만 고르는 방법
# 곱하기 혹은 더하기

# 각자리숫자(0부터9) 로만 이루어진 문자열 S 가 주어졌을때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장큰수를 구하는 프로그램을 작성하세요. 단 + 보다 x 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.


def test():
  S = input()
  index = 0
  result = int(S[0])
  for i in S[1:len(S)]:
    sResult = result + int(i)
    mResult = result * int(i)
    max = sResult if (sResult > mResult) else mResult
    result = max
  return result


# 답안예시
# 해결 아이디어 : 각자리 두수중에 0또는1이면 더하기가 좋고, 아니면 곱하기연산이 낫다
def solution():
  S = input()
  result = int(S[0])
  for i in S[1: len(S)]:
    num = int(i)
    if result <= 1 or num <= 1:
      result += num
    else:
      result *= num
  return result
