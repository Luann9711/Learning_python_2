# Chapter04-01
# 파이썬 심화
# 시퀀스 형과 비시퀀스 타입
# 컨테이너 (Container : 서로 다른 자료형을 담을 수 있음 (List, Tuple, collections.deque))
# Flat : 단일 자료형만 담을 수 있음 (str, bytes, bytearray, array.array, memoryview)
# 시퀀스 자료형 (순서가 있는 자료형)

# 가변형과 불변형으로 나눌 수 있음
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변 (Tuple, str, bytes)

# 리스트 및 튜플 고급


# 지능형 리스트(Comprehending List)
chars ='+_)(*&^%$#'

code_list1 = []

for s in chars:
    # 유니코드 리스트 ord()
    code_list1.append(ord(s))

print(code_list1)

# 지능형 리스트(Comprehending List)
# 한줄로 짜는법
# List comprehension 을 쓰면 약간의 속도상의 이득이 있음
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending Lists + Map, Filter
# filter(function, iterator) // 함수와 그 함수를 실행할 리스트 이렇게 2개의 attribute를 요구한다.
# map(function, list) // 입력 받은 요소의 수행된 결과를 묶어서 반환하는 함수
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(code_list3)
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()

# Geneator 생성
# 작은 메모리조각으로도 연속된 데이터를 만들어낼 수 있다
import array

# Generator :  한번에 한개의 항목을 생성 (메모리 유지를 하지 않음)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(tuple_g)
print(array_g)
print(array_g.tolist())


# Geneator 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(s)


# 리스트 주의 (중요!!)
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] *3 ] * 4
print(marks1)
print(marks2)

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'
print(marks1)
print(marks2)

# id 값 확인
print([id(i) for i in marks1])
print([id(i) for i in marks2])