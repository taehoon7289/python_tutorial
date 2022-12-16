# 두배열의 원소교체

# N: 두배열의 원소개수, K: 교체 횟수
# K번 교체해서 만들수 있는 A 배열의 총합을 최대값

N, K = map(int, input().split())

# print(N, K)
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a의 최소값 k개, b의 최대값 k개를 바꿔치기한다.
a.sort()  # 오름차순
b.sort(reverse=True)  # 내림차순

for i in range(K):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]

result = 0
for i in a:
  result += i

print("총합 : ", result)
