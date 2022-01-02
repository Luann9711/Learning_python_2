# Chapter06-01
# 병행성(Concurrency)
# 이터레이터(Iterator), 제네레이터(Generator)

# 제너레이터는 이터레이터를 반환하는 함수이다 (이터레이터를 생성함)

# 파이썬에서 반복 가능한 타입
# collections, text file, list, set, dict, Tuple, unpacking, *args    ------ iterable

t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(dir(t))

# 반복이 가능한 이유 = iter(t) 함수 호출
# 내부적으로 t가 iter 함수를 호출해서 next 함수를 통해 다음값을 반환
for c in t:
    print(c)


# while
w = iter(t)

print(dir(w)) # 사용가능한 내부 함수들 목록보기

# next 함수가 실행되었기에 위의 for 반복문이 작동
print(next(w))  # A 반환
print(next(w))  # B 반환
print(next(w))  # C 반환


# stpoIteration 예외처리가 발생했을때 반복문 해제
while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()
print()

# 반복형 확인
from collections import abc  # abstractmethod

print(hasattr(t, '__iter__'))

# 반복형 확인 2
# 상속을 받았는지 확인한다
print(isinstance(t, abc.Iterable))

print()

# next (불편쓰)
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration!!!')
        self._idx += 1
        return word

    # def __repr__(self):
    #     return 'WordSplit(%s)' % (self._text)


wi = WordSplitter('Do today what you could do tommorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))


# Using Generator pattern
# 1. 지능형 리스트, 딕셔너리 , 집합 등을 만들 수 있다.  -- 데어터 양 증가 (메모리 사용량 증가) --제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴을 제네레이터 활용가능해야 작성 가능
# 3. 작은 메모리 조각을 사용


class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word  # 제네레이터
        return          # 사실 필요없음
    
    def __repr__(self):
        return 'WorldSplitGenerator(%s)' % (self._text) 


ww = WordSplitGenerator('Do today what you could do tommorrow')

wt = iter(ww)

print(wt, ww)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))

