# Chapter06-03
# 병행성(Concurrency)
# 병렬성(Parallelism)
# 흐름제어, 병행성(Concurrency)
# 코루틴(Coroutine)

# 코투틴 : 단일(싱글)스레드, 스택을 기반으로 동작하는 비동기 작업
# 쓰레드 : OS 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드
# yield : 메인 <-> 서브

# 코루틴 제어, 상태, 양방향 전송
# 서브루틴 :  메인루틴 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소
# 쓰레드 : 싱글스레드 -> 멀티스레드 -> 복잡 -> 공유되는 자원 -> 교착 -> 컨텍스트 스위칭 비용 up

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
# next(cr1)

# 메인 루틴과 서브 루틴이 send() 를 통해서 값 양방향 전송 가능
# 전송값이 따로 없을때 기본 값은 None
# 값 전송
cr1.send(100)  # send 가 next()의 기능도 포함 


# 잘못된 사용

cr2 = coroutine1()

# cr2.send(100) #(next() 사용 없이 send 사용 시 예외발생)