# 현재상황에서 지금 당장 좋은것만 고르는 방법
# 1이 될때까지

# 어떠한 수 N이 1이 될때까지 두 과정중 하나를 반복적으로 선택하여 수행하려고 합니다.
# 단, 두번째 연산은 N이 K로 나누어 떨어질때만 선택할수 있다.

# 1. N에서 1을 뺍니다.
# 2. N을 K로 나눕니다.
# N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야 하는 최소횟수를 구하는 프로그램 작성


def test():
  N, K = map(int, input().split())
  count = 0
  while (N != 1):
    if (N % K == 0):
      N //= K
    else:
      N -= 1
    count += 1
  return count



# 이해하는데 쫌 걸림
# 답안예시
def solution():
  N, K = map(int, input().split())
  result = 0
  while True:
    print("-------")
    # N이 K로 나누어 떨어지는 수가 될때까지 빼기
    target = (N // K) * K
    print(f"target : {target}")
    result += (N - target)
    print(f"result : {result}")
    print("-------")
    N = target
    # N이 K보다 작을때 (더이상 나눌 수 없을때 반복문 탈출)
    if N < K:
      break
    # K로 나누기
    N //= K
    result += 1
    print(f"N : {N}")
  # 마지막으로 남은 수에 대하여 1씩 빼기
  result += (N - 1)
  return result
