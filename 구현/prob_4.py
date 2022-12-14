# 문자열재정렬 

# S: 문자열
# 문자열중 알파벳은 오름차순, 그뒤로 숫자들의 총합을 출력
def test():
  S = input()
  alphas = []
  numbers = []
  for c in list(S):
    if c.isdigit():
      numbers.append(int(c))
    else:
      alphas.append(c)

  alphas.sort()
  result = ''.join(alphas)
  if len(numbers) > 0:
    return result + f"{sum(numbers)}"  
  return result

  

# 답안예시
#
def solution():
  data = input()
  result = []
  value = 0

  for x in data:
    if x.isalpha():
      result.append(x)
    else:
      value += int(x)
  result.sort()
  if value != 0:
    result.append(str(value))
  return ''.join(result)
  

        