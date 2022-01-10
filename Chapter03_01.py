# Chapter03-01
# 파이썬 심화
# Special Method(Magic Method)
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 매직 메소드란?  -  클래스 안에 정의할 수 있는 특정한 메소드


# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))


n = 10

print(n + 180)
print(n.__add__(180))    # 위 n + 180 은 __add__ 라는 매직 메소드가 호출되는 구조로 실행된다.
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n.__mul__(13), n * 13)

print()
print()

# 클래스 예제 1

class Fruit:
    def __init__(self, name , price):
        self._name = name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : Name - {} , Price - {}'.format(self._name, self._price)

    def __add__(self, x):
        return (self._price + x._price)

    def __sub__(self, x):
        return self._price - x._price

    def __mul__(self, x):
        return self._price * x._price

    def __le__(self, x):
        print('Called >> __le__ Method')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('Called >> __ge__ Method')
        if self._price >= x._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit('Apple', 3000)
s2 = Fruit('Banana', 4500)


# 매직메소드 출력
print(s1)
print(s2)

print(s1.__add__(s2))
print(s1.__sub__(s2))
print(s1.__mul__(s2))
print(s1 >= s2)
print(s1 <= s2)