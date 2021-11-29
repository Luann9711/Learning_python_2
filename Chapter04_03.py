# Chapter04-03
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Key에 Value 를 저장하는 구조
# 파이썬에서는 dict 타입이 해쉬테이블의 예시
# 키 값의 연산결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해쉬주소 -> Key 에 대한 value 참조
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화


# dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2))  가변형인 리스트가 있는 곳에서는 hash 함수 사용 불가능

print()
print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)


# Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v) # 오류로그!! : append 함수 다음 []로 쓰지 말 것

print(new_dict2)
