# Chapter03-02
# 파이썬 심화
# Special Method(Magic Method)
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)


# 클래스 예제 2
class Vector(object):
    def __init__(self, *args):
        '''
        Create a vector
        example : v = Vector(5,10)
        '''
        if len(args) == 0:
            self._x, self._y = 0,0
        else:
            self._x, self._y = args
        
    def __repr__(self):
        '''Return the vector infomations.'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Return the sum of the self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        '''Return the times of the self and other'''
        return Vector(self._x * other._x, self._y * other._y)

    def __bool__(self):
        '''Return True if the vector is 0,0 or not 
        (If it is 0,0 returns false)'''
        return bool(max(self._x, self._y))



# Vector 인스턴스 생성
v1 = Vector(5,9)
v2 = Vector(23,636)
v3 = Vector()

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(bool(v1), bool(v2))
print(bool(v3))


print()