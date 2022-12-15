# 현재상황에서 지금 당장 좋은것만 고르는 방법
# 모험가 길드

# N: 모험가 수, X: 공포도
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야함
# N명의 모험가에 대한 정보가 주어졌을때, 여행을 떠날수 있는 그룹수의 최대값은

# -> x가 가장 낮은 사람부터 가능한 그룹수 총합

# 내가 잘못 이해한 방법: 여행을 떠날수 있는 그룹의 최대 경우의 수를 구하는거라고 생각 그래서 조합을 해야되는 걸로 생각함.

import sys


# dict에 공포도를 키로 넣고 같은 공포도 수를 카운팅
# 카운팅 / 공포도 의 몫으로 0이상인 경우들의 합으로 최대 그룹수 체크 가능
def test():
  N = int(input())
  xArray = list(map(int, sys.stdin.readline().split()))
  xArray.sort()

  gCnt = 0
  mCnt = 0
  for x in xArray:
    mCnt += 1
    if (mCnt >= x):
      gCnt += 1
      mCnt = 0
  return gCnt


# 답안예시
#
def solution():
  N = int(input())
  data = list(map(int, input().split()))
  data.sort()

  # 그룹수
  result = 0
  # 그룹의 멤버수
  count = 0
  for i in data:
    # i 는 공포도
    count += 1
    if count >= i:
      # 그룹을 하나 만들지 아니면 그룹에 포함시킬지 조건
      result += 1
      count = 0

  return result
