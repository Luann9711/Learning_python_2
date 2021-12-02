# Chapter04-04
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict
from types import MappingProxyType  # making immutable Dict

f = {'key1': 'number1'}
print(type(f))

# read only
f_frozen = MappingProxyType(f)

print(f, id(f))
print(f_frozen, id(f_frozen)) # 객체를 복사해서 다른 주소값에 할당후 froze

# 수정 불가
# f_frozen['key2'] = 'number2'


# 수정 가능
f['key2'] = 'number2'
print(f)

print()

s1 = {'Apple', 'Banana', 'Orange', 'Kiwi', 'Apple'}
s2 = set(['Apple', 'Banana', 'Orange', 'Kiwi', 'Apple'])
s3 = {3}
s4 = set()
# 중복되어서도 안되고 값변경이 일어나서는 안되는 중요한 데이터들은 forzenset 으로 얼리면 MappingProxyType을 적용한 것과 같은 효과를 지님
s5 = frozenset({'Apple', 'Banana', 'Orange', 'Kiwi', 'Apple'}) 


print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))
print(type(s5))


# 선언 최적화
# 파이썬은 실행될때 파이썬 인터프리터가 바이트코드를 실행
from dis import dis

print('-----------------------')
print(dis('{10}'))
print(dis('set([10])'))


# 지능형 집합 (comprehending set) --------------------
from unicodedata import name
print({name(chr(i),'') for i in range(0,256)})
print({chr(i) for i in range(0,500)})