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

from greedy.prob_4 import test, solution
print(test())
print(solution())