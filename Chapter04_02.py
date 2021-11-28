# Chapter04-02
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque]
# Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])

# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급
#==============================================================================================
# Tuple Advanced
# Unpacking

# b, a = a, b
print(divmod(100, 9))
print(divmod(*(100,9)))  # 튜플 앞에 쓰는 *는 언팩킹
print(*(divmod(100,9)))  # 튜플로 반환하는 divmod 를 언팩킹 함

print()

x, y, *rest = range(10)
print(x, y, rest)  # rest는 할당된 값들을 묶어서 리스트로 반환한다

x, y, *rest = range(2)
print(x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)
# 리스트의 경우에는 가변형이기에 값이 변해도 같은 주소값에서 수정해서 실행하는데
# 튜플같이 불변형일 경우에는 값이 변할때 마다 새로운 주소값에서 실행하기 떄문에 효율적이지 못하다
# 변동성이 많은 데이터의 경우엔 리스트로 묶는 것이 자원활용면에서 유리
l = (15, 20, 25)
m = [15, 20, 25]

print(m, id(m))
print(l, id(l))

l = l * 2
m = m * 2

print(m, id(m))
print(l, id(l))

l *= 2
m *= 25

print(m, id(m))
print(l, id(l))

print()
print()

# sort vs sorted
# reverse /반대로 정렬, key=len, key=str.lower, key=function()

# sorted: 정렬 후 새로운 객체로 반환  (원본은 수정되지 않음)
f_list = ['orange', 'apple', 'banana', 'strawberry', 'lemon', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - ', sorted(f_list, key = lambda x : x[-1]))
print('sorted - ', sorted(f_list, key = lambda x : x[-1], reverse=True))
print(f_list)
print()

# sort: 정렬 후 객체 직접 변경 (원본수정)
# 반환 값 확인(none)
print('sort - ', f_list)
print('sort - ', f_list.sort())
print('sort - ', f_list)
print('sort - ', f_list.sort(reverse = True),f_list)
print('sort - ', f_list.sort(key = lambda x: x[-1]),f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)