# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1.런타임 초기화 
# 2.변수 할당 가능
# 3.함수 인수 전달 가능
# 4.함수 결과 반환 가능 (return)

# 함수객체
def factorial(n):
    '''Factorial function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)
    # 재귀함수


class A:
    pass

print(factorial(5))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial

print(var_func)
print(map(var_func, range(1,20)))
print(var_func(10))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위함수(Higher-order function)
# map, filter, reduce 등
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

# reduce 함수  - 누적값 계산에 사용
from functools import reduce
from operator import add

print(reduce(add, range(1,11)))
print(sum(range(1,11)))

# 익명함수(lambda)
# 가급적 주석 활용
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x + t, range(1,1025)))

# Callable : 호출 연산자 - > 메소드 형태로 호출가능한지 확인
# 호출 가능 확인
print(callable(str), callable(len))

# partial 사용법 : 인수고정 -> 콜백함수 사용
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정

five  = partial(mul, 5)
print(five(14))

print([five(i) for i in range(1, 257)])