# Chapter06-03
# 병행성(Concurrency)
# 병렬성(Parallelism)
# 흐름제어, 병행성(Concurrency)
# 코루틴(Coroutine)

# 코투틴 : 단일(싱글)스레드, 스택을 기반으로 동작하는 비동기 작업
# 쓰레드 : OS 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드
# yield <-> send : 메인 <-> 서브

# 코루틴 제어, 상태, 양방향 전송
# 서브루틴 :  메인루틴 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소
# 쓰레드 : 싱글스레드 -> 멀티스레드 -> 복잡 -> 공유되는 자원 -> 교착 -> 컨텍스트 스위칭 비용 up
# def -> async , yield -> await

# 서브 루틴
# 코루틴 Ex 1
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))


# 메인 루틴
# 제네레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
next(cr1)
# next(cr1)

# 메인 루틴과 서브 루틴이 send() 를 통해서 값 양방향 전송 가능
# 전송값이 따로 없을때 기본 값은 None
# 값 전송
# cr1.send(100)  # send 가 next()의 기능도 포함 


# 잘못된 사용
# cr2 = coroutine1()
# cr2.send(100) #(next() 사용 없이 send 사용 시 예외발생)


# 코루틴 Ex 2
# GEN_CREATED :  처음 대기 상태
# GEN_RUNNING :  실행상태
# GEN_SUSPENDED : Yield 대기 상태
# GEN_CLOSED :  실행완료 상태

def coroutine2(x):
    print('>>> coroutine2 started : {}'.format(x))
    y = yield x
    print('>>> coroutine2 received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine2 received : {}'.format(z))
    t = yield


cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))
print(next(cr3))

# print(getgeneratorstate(cr3))
# cr3.send(1000)

# print(next(cr3))
# print(getgeneratorstate(cr3))
# cr3.send(1500)


print()
print()


# 코루틴 Ex 3
# StopIteration 자동처리(3.5 이상에선 await 으로 자동 처리)
# 중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y


t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))

t2 = list(generator1())
print(t2)

print()
print()


def generator2():
    yield from 'ABCD'
    yield from range(1,10)

t3 = generator2()
t4 = list(generator2())

print(next(t3))
print(next(t3))
print(t4)