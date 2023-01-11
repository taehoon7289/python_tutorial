# import sys

# # sys.stdin.readline

# print("hello world!")

# print(1e9)  # 실수로 나옴 10억

# print(int(1e9))  # 정수

# print(5e-1)

# print(1 / 3)

# print((1 / 3) * 1e1)

# print(round((1 / 3) * 1e1, 2))

# print(True)

# print(False)

# print(5 % 2)  # 1
# print(5 // 2)  # 2
# print(5**2)  # 25

# list1 = [1, 2, 3, 4, 5, 6, 7]
# print(list1)
# print(list1[-1])

# n = 1
# list2 = [3] * 5
# print(list2)

# print(list1[1:4])
# print(list1)

# list3 = [i for i in range(0, 10, 1)]
# print(list3)
# list3.sort(reverse=True)
# print(list3)

# for i in range(1, 10, 2):
#   print(i)

# array = [[i] * 4 for i in range(1, 10)]
# print(array)
# print(array.count([2, 2, 2, 2]))  # 동일한 개수

# print("hellowold")
# print('hellowold')
# print("\"hellowold\"")

# print("hello world!\n" * 10)

# tuple = (1, 2, 3, 4, 5, 6)
# print(tuple)
# print(tuple[4])
# # tuple[4] = 8 # 튜플은 값 변경 불가

# data = dict()
# data['one'] = 1
# data['two'] = 2
# data['three'] = 3

# print(data)

# if "two" in data:
#   print(data['two'])

# keys = data.keys()
# print(keys)
# print(data.values())

# obj = {'name': 'ddd', 'age': 36}

# print(obj)
# print(obj.keys())
# print(obj.values())

# # 집합자료형 set

# temp = set({1, 23, 4, 5, 6, 6})
# print(temp)

# temp2 = set([1, 23, 4, 5, 6, 6])
# print(temp2)

# temp3 = {1, 23, 4, 5, 6, 6}
# print(temp3)

# # set에서 add, update, remove 메소드, & + - 연산 사용가능

# # 기본 입출력

# # inputMap = map(int, input().split())
# # print(inputMap)
# # print(list(inputMap))

# # n = input()
# # inputs = list(map(int, input().split()))
# # print(n)
# # print(inputs)

# # test = input()
# # print(test)

# # data1 = sys.stdin.readline()
# # print(data1)
# # print(11 , 2 ,23, end = "endendend")

# number = 0
# print(f"dfkjrjewofms {number} dsfksdfk1")

# if (number > 0):
#   print('okok')
#   # pass
# elif (number == 0):
#   print('okokokok')
# else:
#   print('nonono')

# print(True and False)

# print(True or False)

# print(not True)

# print(not False)

# if (0 < number < 20):
#   print("good")

# count = 0
# while count <= 10:
#   count += 1
#   print(count)

# count = 0

# for i in range(11):
#   count += 1
#   print(count)

# count = 0

# while count == 0:
#   print("탈출!!")
#   break

# def customSum(a=0, b=0):
#   # global count
#   # count = 300
#   print(f"sum 호출됨 {a}, {b}, {count}")
#   return a + b

# print(customSum(10, 20))

# print(customSum(10))

# print(customSum(b=10, a=5))

# def packing():
#   a = 1
#   b = 2
#   c = 3
#   d = 4
#   return a, b, c, d

# print(packing()[1])

# # 람다식 사용 방법
# lambdatemp = lambda a, b: a - b

# print(lambdatemp(1, 2))

# temptemp = [1, 2, 3, 4]

# print(list(map(lambda a: a * 3, temptemp)))

# # import 방식도 약간 다름
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# data = ['a', 'b', 'c']
# # 조합
# result = list(combinations(data, 2))
# print(result)

# # 중복순열
# result = list(product(data, repeat=2))
# print(result)

# # 중복조합
# result = list(combinations_with_replacement(data, 2))
# print(result)

# from collections import Counter

# counter = Counter(
#   ['red', 'red', 'red', "blue", "blue", "blue", "blue", "blue", "green"])

# print(counter['red'])
# print(counter['blue'])
# print(counter['green'])

# from greedy.prob_1 import test, solution
# print(f"{test()} 개")
# print(f"{solution()} 개")
# from greedy.prob_2 import solution
# print(test())
# print(solution())

# from greedy.prob_3 import solution
# print(test())
# print(solution())

# stack = []
# stack.append(1)
# print(stack)
# stack.append(2)
# print(stack)
# stack.append(3)
# print(stack)
# stack.append(4)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.append(5)
# print(stack)
# stack.pop()
# print(stack[::-1])  # 마지막 부터 출력

# stack = []
# print(stack.append(1))  # return None
# print(stack.pop())  # pop 하면 마지막 value return

# from collections import deque
# # 큐 (순차적으로 의미)
# queue = deque()
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue.popleft())
# print(queue)
# queue.append(4)
# print(queue.popleft())
# print(queue)

# queue.reverse()

# print(queue)

# # 재귀함수 : 자기자신을 호출 recursive function
# def recursiveFn(n):
#   if n < 1:
#     return
#   print(f"This is recursiveFn : {n:03d}")
#   recursiveFn(n - 1)

# recursiveFn(100)

# 유클리드 호제법
# 두 자연수 a,b 에 대해 a>b 일때 a를 b로 나눈 나머지가 r일때,
# a, b의 최대공약수는 b와 r 의 최대공약수와 같다.

# 192, 162

# 유클리드 호제법을 이용한 재귀함수식
# def gcdFn(a, b):
#   r = a % b
#   if r != 0:
#     print(f"b : {b}, r: {r}")
#     return gcdFn(b, r)
#   return b

# print(gcdFn(192, 162))

# DFS (깊이우선탐색)
# start
# 방문처리
# 이후 인접노드 찾기 (인접노드란? 방문하지 않은 노드 있는지)
#   인접노드 없으면 끝
#   인접노드 있으면 인접노드중 하나 start 처리

# row = 5
# column = 3
# array = [[0 for i in range(column)] for j in range(row)]
# print(array)
# array[0][0] = 1
# print(array)

# array2 = [[0] * column] * row
# print(array2)
# array2[0][0] = 1
# print(array2)

# BFS(너비우선탐색) -> 큐 사용
# 인접노드 큐 삽입 후 방문처리(큐에서 꺼내면서 인접노드 탐색)

# nodes = [i for i in range(1, 10)]
# print(nodes)
# visited = [False for i in range(1, 10)]

# print(visited)
# visited[0] = True
# visited[5] = True
# print(visited)

# import 탐색.prob_1_sol
# print(test())
# print(solution())

# import 탐색.prob_1_sol

# import 탐색.prob_2_sol

# 정렬
data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# # 선택정렬 : 지금 리스트에서 가장 작은거 찾아서 가장 앞으로 보냄
# print("before : ", data)
# for i in range(len(data) - 1):
#   # min = data[i]
#   minIndex = i
#   for index in range(i, len(data)):
#     if data[minIndex] > data[index]:
#       # min = data[index]
#       minIndex = index
#   # data.insert(i, data.pop(minIndex))
#   # 파이썬 스왑
#   data[i], data[minIndex] = data[minIndex], data[i]
# print("after : ", data)
# 삽입정렬 : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
# 타겟 대상의 왼쪽은 이미 정렬되어 잇다라고 가정한상태로 위치를 정해서 삽입

# for i in range(1, len(data)):
#   for j in range(i):
#     # data[i] : 타겟 대상
#     # data[j] : 이미 정렬된 대상들
#     print("target : ", data[i])
#     # print("target index : ", i)
#     if data[j] < data[i] <= data[j + 1]:
#       data.insert(j + 1, data.pop(i))
#       print(f"{j}번째에 {data[j]} 넣음")
#       print("ing : ", data)
#       break
#     elif data[0] > data[i]:
#       # print("data[0]", data[0])
#       # print("data[i]", data[1])
#       data.insert(0, data.pop(i))
#       print(f"0번째에 {data[0]} 넣음 --")
#       print("ing : ", data)
#       break

# print("after :", data)

# for i in range(1, len(data)):
#   for j in range(i, 0, -1):
#     # 타겟값에서 왼쪽방향으로 진행
#     # 타겟 : data[j]
#     if data[j] < data[j - 1]:
#       # 스왑
#       data[j], data[j - 1] = data[j - 1], data[j]
#       # 스왑하고 또 더 타겟보다 큰게 있을수 있으니까 재 진행
#     else:
#       # 타겟보다 큰게 아니면 이미 정렬 된리스트중이 나보다 작은게 없다는 의미
#       break
# print("after :", data)

# 퀵정렬
# 기준데이터를 고르고 큰데이터와 작은 데이터 위치를 바꿈
# 기준데이터를 기준으로 분할 작업 (재귀함수 사용)

# import time

# def quickSort(start, end):
#   if start >= end:
#     return
#   pivot = start
#   leftIndex, rightIndex = start + 1, end
#   print("pivot : ", data[pivot])
#   while leftIndex <= rightIndex:
#     while leftIndex <= end and data[leftIndex] <= data[pivot]:
#       leftIndex += 1
#     while rightIndex > start and data[rightIndex] >= data[pivot]:
#       rightIndex -= 1

#     if leftIndex > rightIndex:
#       print("pivot swap", leftIndex, rightIndex)
#       data[rightIndex], data[pivot] = data[pivot], data[rightIndex]
#     else:
#       print("swap : ", data[leftIndex], data[rightIndex])
#       data[leftIndex], data[rightIndex] = data[rightIndex], data[leftIndex]
#       print("ing : ", data)
#   print("분할시 start rightIndex", start, rightIndex)
#   quickSort(start, rightIndex - 1)
#   quickSort(rightIndex + 1, end)

# quickSort(0, len(data) - 1)
# print("after :", data)

# 계수정렬
# 특정한 조건이 부합할때만 사용할수 있음.
# data = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# obj = {}
# for digit in data:
#   # obj[digit] = 0
#   print(obj.get(digit))
#   if obj.get(digit) == None:
#     obj[digit] = 0
#   obj[digit] += 1
# print(obj)

# max = max(data)
# print(max)
# cntArray = [0 for i in range(max + 1)]

# for digit in data:
#   cntArray[digit] += 1
# print(cntArray)

# result = ""
# for index in range(len(cntArray)):  # 값
#   for i in range(cntArray[index]):  # 횟수
#     result += f"{index}"
# print(result)

# import 정렬.prob_1

# data = [15, 213, 3, 10, 345, 313, 6, 0, 12, 334, 45, 39, 324, 64]
# 선택정렬 : 지금 리스트에서 가장 작은거 찾아서 가장 앞으로 보냄
# print("before : ", data)
# for i in range(1, len(data)):
#   for j in range(i):
#     # data[i] : 타겟 대상
#     # data[j] : 이미 정렬된 대상들
#     if data[j] < data[i] <= data[j + 1]:
#       data.insert(j + 1, data.pop(i))
#       break
#     elif data[0] > data[i]:
#       data.insert(0, data.pop(i))
#       break
# print("after :", data)

# def quickSort(start, end):
#   if start >= end:
#     return
#   pivot = start
#   leftIndex, rightIndex = start + 1, end
#   while leftIndex <= rightIndex:
#     while leftIndex <= end and data[leftIndex] <= data[pivot]:
#       leftIndex += 1
#     while rightIndex > start and data[rightIndex] >= data[pivot]:
#       rightIndex -= 1

#     if leftIndex > rightIndex:
#       data[rightIndex], data[pivot] = data[pivot], data[rightIndex]
#     else:
#       data[leftIndex], data[rightIndex] = data[rightIndex], data[leftIndex]
#   quickSort(start, rightIndex - 1)
#   quickSort(rightIndex + 1, end)

# data = [15, 213, 3, 10, 345, 313, 6, 0, 12, 334, 45, 39, 324, 64]
# print("before : ", data)
# quickSort(0, len(data) - 1)
# print("after :", data)

# n = 100
# print([i for i in range(n + 1) if i % 2 != 0])

# 최소공배수, 최대공약수 외우기
a, b = 10, 32
x, y = a, b
while y:
  x, y = y, x % y
  print(x, y)
print("gcd : ", x)
print("lcm :", (a * b) // x)

# 비트연산자
# init = 3
# for i in range(10):
#   print("i :: ", init << i)

# print([0,1,2,3,4,5,5].count(4))
# print('가나다라마바사다다다'.count('다'))

# array = [0]
# array += [33]
# array += [66]
# array += [8]
# array.append([11,2,3,4])
# print(array)

# x = 12
# d = 2
# while d <= x:
#   if x % d == 0:
#     x //= d
#     print("???", d)
#   else:
#     d += 1
#     print("###", d)

# n = 12
# nums = set([])
# d = 2
# while n<=d:
#   if n % d == 0:
#     n //= d
#     nums.add(d)
#     print(d)
#   else:
#     d += 1
#   print("n", n)
# print(nums)
# print('???')

# n = 145
# d = 2
# while d <= n:
#   if n % d == 0:
#     n //= d
#     print(d)
#   else:
#     d += 1

# temp = '1 -2 -3 -4 -5 -6 -7 -8'
# print(sum(list(map(int, temp.split()))))

# d = 'da'
# spell = 'bcda'
# print(d in spell)

# print(type('1'))
# print(type(1))
# print(type(1.0))

# a = [0, 'f']
# a[0] = 'd'
# a[1] = 4
# print(a)

# array = [1,2,3,4,5,6,7]
# print(array[0:len(array)-2:-1])
# print(array[-1])
# print(array[0:3:-3])
# print(array[:3:-2])

# a = [0,0,0]
# print(a[-1])

# temp = "adcdefg"
# print(temp*2)

# # print(int("3-7+88"))

# a = [1,2,3,5]
# b = [0,3,6,7,8,9,1,2,3,4]
# # print(set(a) - set(b))
# print(b.index(3))

# temp = 'temp'
# print('flag', 'tm' in temp)

# temp = [[0,0,0,0], [1,1,1,1],[2,2,2,2]]
# print(len(temp))
# print(len(temp[0]))

# 순서유지하면서 중복제거후
# temp = "kimtaehoon"
# result = ""
# for c in temp:
#   if c not in result:
#     result += c
# print(result)

# a = ['a']
# temp = ['ee','c','b','aa', 'd', 'ee']
# result = []
# for t in temp:
#   print(t)
#   if t not in result:
#     result.append(t)
# print(result)


# from collections import Counter
# temp = ['c','b','aa', 'd', 'ee', 'ee', 'a', 'a', 'a', 'a', 'a']
# temp2 = ['ee','c','b','aa', 'd', 'a', 'v', 'v', 'v']
# print(Counter(temp) - Counter(temp2))
# # print(Counter(temp))
# # print(Counter(temp).most_common(2))

# ttt = 'abcdefg'
# a = ['aa', 'bb', 'cccc']
# print(Counter(a))
# obj = {}
# obj['1'] =1
# obj['2'] =2
# obj['3'] =3
# obj['4'] =4
# obj[4] =44

# if 4 in obj:
#   print('on')
# else:
#   print('off')

from collections import Counter

# temp = ['111', '22', '111']
# print(Counter(temp))
# print(temp.count('1'))


# array = [i for i in range(10)]
# for a in range(len(array)):
#   # print(a)
#   array.remove(array[a])
#   print(array)
# # print("---")
# # for a in range(len(array)-1,-1,-1):
# #   print(a)



print("-------------------------")
array = [i for i in range(10)]
print(array)
# for a in range(len(array)):
#   # print(a)
#   array.remove(array[a])
#   print(array)



# for a in array:
#   array.remove(a)
#   print(array)
# print(array)

# while array:
#   array.remove(array[0])
#   print(array)
# print(array)

# temp = ['3', '34', '35', '32', '30', '31', '234', '2']
# temp = [3,34,35,32,30,31,234,2]
# temp.sort(reverse = True)
# print(temp)
# print(list(map(min, enumerate(temp, start = 1))))

# print(list(map(lambda s: s*4, temp)))
# print(sorted(temp, reverse = True))
# temp = [1,2,3,4]
# # print(temp[3:])
# for i, v in enumerate(reversed(temp)):
#   print(i, v)

# # 유클리드호제법 다시
# a, b = 100, 50
# x, y = a, b
# while y:
#   x, y = y, x % y
#   print(x, y)
# print("최대공약수: ", x)
# print("최소공배수: ", a * b // x)

# temp = []
# print(temp + [1] + [2])
# temp = [1,23,4]
# print(temp + [3])

# from heapq import heappop, heappush
# array = []
# for v in [[5.5,4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2], [0,0,2,1,2], [0,-1,2,1,2], [-1,-1,2,1,2]]:
#   heappush(array, v)
# print(array)
# while array:
#   print(heappop(array))


# from collections import deque
# from heapq import heappush, heappop
# def solution(alp, cop, problems):
#     answer = 0
#     max_alp = max([p[0] for p in problems])
#     max_cop = max([p[1] for p in problems])
#     results = []
#     tasks = deque()
#     temps = search_problems(alp, cop, problems, max_alp, max_cop)
#     while temps:
#         prop = heappop(temps)
#         tasks.append([alp + prop[3], cop + prop[4], prop[5]])
#     while tasks:
#         value = tasks.popleft()
#         v_alp, v_cop, v_t = value
#         print('tasks len :', len(tasks))
#         print('v_alp, v_cop, v_t', v_alp, v_cop, v_t)
#         if v_alp >= max_alp and v_cop >= max_cop:
#             results.append([v_alp, v_alp, v_t])
#             print('results', [v_alp, v_alp, v_t])
#         else:
#             result_props = search_problems(v_alp, v_cop, problems, max_alp, max_cop)
#             while result_props:
#                 prop = heappop(result_props)
#                 print('tasks append', [v_alp + prop[3], v_cop + prop[4], v_t + prop[5]])
#                 tasks.append([v_alp + prop[3], v_cop + prop[4], v_t + prop[5]])
#     if results:
#         return results[0][2]
#     return answer

# def search_problems(alp, cop, problems, max_alp, max_cop):
#     need_alp, need_cop = max_alp - alp, max_cop - cop
#     avail_props = [p for p in problems if p[0] <= alp and p[1] <= cop]
#     avail_props.append([0,0,1,0,1])
#     avail_props.append([0,0,0,1,1])
#     result_props = []
#     if need_alp > 0 and need_cop > 0:
#         for prob in avail_props:
#             min_alp, min_cop, rwd_alp, rwd_cop, t = prob
#             temp = [int((rwd_alp+rwd_cop) // t), min_alp, min_cop, rwd_alp, rwd_cop, t]
#             heappush(result_props, temp)
#     elif need_alp > 0:
#         for prob in avail_props:
#             min_alp, min_cop, rwd_alp, rwd_cop, t = prob
#             temp = [int(rwd_alp // t), min_alp, min_cop, rwd_alp, rwd_cop, t]
#             heappush(result_props, temp)
#     elif need_cop > 0:
#         for prob in avail_props:
#             min_alp, min_cop, rwd_alp, rwd_cop, t = prob
#             temp = [int(min_cop // t), min_alp, min_cop, rwd_alp, rwd_cop, t]
#             heappush(result_props, temp)
#     else:
#         print('else alp, cop', alp, cop)
#     return result_props

# from collections import deque
# from heapq import heappush, heappop
# def solution(alp, cop, problems):
#     answer = 0
#     max_alp = max([p[0] for p in problems])
#     max_cop = max([p[1] for p in problems])
#     results = []
#     # 문제들중 가장 풀기에 가장 적합한 문제 선정
#     result_flag = False
#     while not result_flag:
#         prop = search_prop(alp, cop, problems)
#         print("prop2", prop)
#         alp += prop[2]
#         cop += prop[3]
#         answer += prop[4]
#         if max_alp <= alp and max_cop <= cop:
#             result_flag = True 
    
#     return answer

# def search_prop(alp, cop, problems):
#     print('search_prop alp, cop', alp, cop)
#     no_avail_probs = [i for i in problems if i[0] > alp and i[1] > cop]
#     reach_props = []
#     avail_probs = [i for i in problems if i[0] <= alp and i[1] <= cop]
#     if not avail_probs:
#         avail_probs.append([0,0,1,0,1])
#         avail_probs.append([0,0,0,1,1])
#     for p in no_avail_probs:
#         for avail_prob in avail_probs:
#             p_a, p_c = p[0] - avail_prob[0], p[1] - avail_prob[1] # 풀려면 높여야되는 능력 수치
#             if p_a > 0 and p_c > 0:
#               reach_props.append([(p_a, p_c), *p])
#     print(reach_props)
#     temps = []
#     for reach_prop in reach_props:
#         for avail_prob in avail_probs:
#             temp = [0, reach_prop[0][0], reach_prop[0][1], avail_prob]
#             print("temp", temp)
#             while temp[1] > 0 and temp[2] > 0:
#                 temp[1] -= avail_prob[2]
#                 temp[2] -= avail_prob[3]
#                 temp[0] += 1
#             temps.append(temp)
#     temps.sort()
#     print('tempstemps', temps)
#     return temps[0][3]

# import heapq
# def solution(alp, cop, problems):
#     answer = 0
#     queue = []
#     problems.append([0,0,1,0,1])
#     problems.append([0,0,0,1,1])
#     max_alp = max([i[0] for i in problems])
#     max_cop = max([i[1] for i in problems])
    
#     heapq.heappush(queue, [0, alp, cop])
#     # print(max_alp, max_cop)
#     while queue:
#         it = heapq.heappop(queue)
#         # print("it", it)
#         t, v_alp, v_cop = it
#         print('it', t, v_alp, v_cop)
        
#         v_alp = min(v_alp, max_alp)
#         v_cop = min(v_cop, max_cop)
        
#         if max_alp <= v_alp and max_cop <= v_cop:
#             # print('v_alp, v_cop', v_alp, v_cop)
#             answer = t
#             break
#         # print('???')
#         for prob in problems:
#             min_alp, min_cop, rwd_alp, rwd_cop, cost = prob
#             # print('min_alp, min_cop', min_alp, min_cop)
#             if min_alp <= v_alp and min_cop <= v_cop:
#                 heapq.heappush(queue, [t + cost, v_alp + rwd_alp, v_cop + rwd_cop])
    
#     return answer
        
# # print('solution', solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))

# # print('dd', float('inf') *10)

#   # print([[INF]*(5 + 1) for _ in range(10 + 1)])
# dp = [[float('inf')]*(5 + 1) for _ in range(10 + 1)]
# print(dp)

# from collections import deque
# def solution(n, paths, gates, summits):
#     answer = []
#     queue = deque()
#     paths = list(map(lambda p: [*p, 0], paths))
#     for g in gates:
#         # [intensity, 지나온 n queue, 지나온 w queue, visited_summit]
#         queue.append([0, [g], [], False, paths])
#     results = []
    
#     while queue:
#         val = queue.popleft()
#         start_node = val[1][0]
#         now_node = val[1][-1]
#         pts = val[4]
#         # print('pts', pts)
#         for i, p in enumerate(pts):
            
#             if (p[0] == now_node or p[1] == now_node) and p[3] < 3:
#                 end_node = p[1]
#                 if p[1] == now_node:
#                     end_node = p[0]
                
#                 if end_node == start_node and val[3]:
#                     # 끝이라면
#                     pts[i][3] += 1
#                     results.append([max(val[0], p[2]), val[1] + [end_node], val[2] + [p[2]], val[3], pts])
                    
#                     continue
#                 if not val[3]:
#                     # 아직 정상 도착 안함
#                     if end_node not in gates:
#                         if end_node in summits:
#                             val[3] = True
#                         pts[i][3] += 1
#                         queue.append([max(val[0], p[2]), val[1] + [end_node], val[2] + [p[2]], val[3], pts])
#                 else:
#                     # 정상 들렸다옴
#                     if end_node not in gates and end_node not in summits:
#                         pts[i][3] += 1
#                         queue.append([max(val[0], p[2]), val[1] + [end_node], val[2] + [p[2]], val[3], pts])
            
#     print(results)


# solution(6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5])


# temps = [[1,2,5],[1,2,2],[1,2,3],[1,2,1],[1,2,4]]
# result = []
# for temp in temps:
#   print(''.join(temp))
#   if temp[0:2] not in result:
#     result += [temp]
# print('test', result)

# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     # 1초당 1 length 씩 이동
#     answer = 0
#     arrive_arr = deque()
#     bridge_arr = deque()
#     start_queue = deque(truck_weights)
#     while start_queue or bridge_arr:
        
#         if bridge_arr and bridge_arr[0][0] >= bridge_length:
#             arrive_arr.append(bridge_arr.popleft())
#         for t in bridge_arr:
#             t[0] += 1
#         now_weight = sum(map(lambda a: a[1], bridge_arr))
#         print('now_weight', now_weight)
#         if now_weight + start_queue[0] <= weight:
#             bridge_arr.append([1, start_queue.popleft()])
        
#         answer += 1
    
#     return answer
# # solution(2,	10,	[7,4,5,6])
# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# # print(list(min(s) for s in sizes))
# print(sum(sizes, [])) # 배열 flat처리

# node = dict({
#   1: {
#     'l': [],
#     'r': [],  
#     },
#   })

# temp = [2,3]

# for i in temp:
  
#   if 2 >= i:
#     n = node.copy()
#     if i % 3 == 0:
#       n[1]['l'].append(n)
#     else:
#       n[1]['r'].append(n)
#     break
#   d = 2
#   while i > d:
#     if i % d == 0:
#       n = node.copy()
#       n[i] = i
#       if i % 3 == 0:
#         n[i]['l'].append(n)
#       else:
#         n[i]['r'].append(n)
#       break
#     else:
#       d += 1

# print(node)
# print(node[1]['r'])
# print(node[1]['r'][0])
# print(node[1]['r'][0][1])
# print(node[1]['r'][0][1]['r'])

# print('helloworld')

word = 'helloworld'
if 'h' in word:
  print('yes')
else:
  print('no')

print(word.upper())
print(word)
print(word[0].lower())
print(word[1].upper())