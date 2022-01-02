# Chapter05-04
# 파이썬 심화
# 데코레이터 (장식자)

# 장점
# 1. 중복제거, 코드 간결, 공통함수 작성
# 2. 로깅, 프레임워크, 유효성체크 -> 공통 기능으로 분리 개발 가능
# 조합해서 사용 용이

# 단점
# 1. 남용시 가독성 감소 가능
# 2. 특정 기능에 한정된 함수는  -> 단일 함수로 작성하는 것이 유리할 수도 있다.
# 3. 디버깅 불편

# 데코레이터 실습
# 함수 실행시간 측정
import time

def pref_clock(func):
    def perf_clocked(*args):
        # 함수 시작시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))


        return result
    return perf_clocked

@pref_clock
def time_func(start_number):
    a = 0
    for i in range(start_number, 1001):
        a += 1
        
    return a

@pref_clock
def some_func(*numbers):
    return sum(numbers)


# 데코레이터 미사용
# none_deco1 = pref_clock(time_func)
# none_deco2 = pref_clock(some_func)

# # print(none_deco1, none_deco1.__code__.co_freevars)
# # print(none_deco2, none_deco2.__code__.co_freevars)

# print('-' * 30,  'Called None Decorator -> time_func')
# print()
# none_deco1(100)
# none_deco2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# print()

# 데코레이터
print('-' * 30,  'Called Decorator -> time_func')
print()
time_func(350)
some_func(100, 200, 300, 400, 500)