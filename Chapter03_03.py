# Chapter03-03
# 파이썬 심화
# 데이터 모델(Data Model)
# 참조 : https://docs.python.org/3/reference/datamodel.html
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# Namedtuple 실습

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체는 id, type -> value 으로 확인할 수 있다


# 일반적인 튜플 사용
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) **2 + (pt1[1] - pt2[1]) **2)

print(l_leng1)



# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언 1
Point = namedtuple('Point', 'x y')

# 두 점 선언
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)


# 두점 사이의 거리 계산
l_leng2 = sqrt((pt3.x - pt4.x)**2 + (pt3.y - pt4.y)**2)

print(l_leng2)


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y z')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default=False

print(Point1,Point2,Point3,Point4)
print()

# Dict to Unpacking
temp_dict = {'x': 46, 'y': 9458889, 'z': 334328}
# 객체 생성
p1 = Point1(10, 35)
p2 = Point2(34, 52)
p3 = Point3(24, 25, 36)
p4 = Point4(1, 2, 3, 4)
p5 = Point3(**temp_dict)  # 언팩킹

print('---------------------')
print(p1, p2, p3, p4, p5)

# 사용
print(p1[0] +p3[1])
print(p1.x + p3.y)
print(p4.x + p1.y)

x, y, z = p5
print((x + y)/z)


# 네임드 튜플 메소드  (_make) //기본 메소드
temp = [52, 34]

p4 = Point1._make(temp)
print(p4)


# _fields :  필드네임 확인
print(p1._fields, p2._fields)


# _asdict() : OrderedDIct 반환 - 네임드튜플을 딕셔너리로 변환
print('return to dict : {}'.format(p1._asdict()))
print(p3._asdict())
print(p3)


# 실 사용 실습
# 반당 20명 학생  / 4개 반(A,B,C,D)
Classes = namedtuple('Classes', ['rank', 'number'])


# # 그룹리스트 선언
# numbers = [str(n) for n in range(1, 21)]

# ranks = 'A B C D'.split()


# # 학생 리스트 생성
# students = [Classes(rank, number) for rank in ranks for number in numbers]

# print(len(students))

# for s in students:
#     print(s)

# 추천 코딩 방식 (이전 학생 리스트 생성법과 결과는 동일함)
students2 = [Classes(rank, number)
                    for rank in 'A B C D'.split()
                        for number in [str(n)
                            for n in range(1, 21)]]

print(len(students2))

for i in students2:
    print(i)



# 응용  (데이터를 파일에 기록)
import csv

with open('./practice/testfile.txt', 'w', encoding='utf8') as studentinfo:

    # fields = ('Rank', 'Student Number')
    # Dic writer
    wt = csv.writer(studentinfo)
    # Header writer
    # wt.writeheader()

    for v in students2:
        wt.writerow(v)



