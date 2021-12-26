# Chapter05-02
# 파이썬 심화
# 클로저 기초

# 파이썬 변수 범위(scope)

# 예제 1
def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(10)

# 예제 2
b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(30)

print('---------------------------')

# 예제 3

c = 30

def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40 
    # 안에 같은 이름이 있을때 print 이후에 선언 되는 변수의 경우에는
    # global 키워드가 없으면 참조전에 할당 되었기 때문에 에러가 발생한다


print('>>',c)
func_v3(10)
print('>>>',c)


# Closure(클로저) 사용 이유
# 함수 내부의 로컬 변수 값을 기억한다
# 서버 프로그래밍 -> 동시성(Concurrency)제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 언어를 사용-> Erlang
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점

a = 100

print(a + 100)
print(a + 1000)
print('----------------------')

# 결과 누적(함수 사용)
print(sum(range(1, 51)))
print(sum(range(51,101)))


# 클래스 사용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# 인스턴스 생성
averager_cls = Averager()

# 누적
# _series 라는 리스트를 이용해서 값을 계속 저장하여 가지고 있을 수 있다  - 클로저
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(1020))

