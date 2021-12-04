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