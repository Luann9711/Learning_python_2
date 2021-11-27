# Chapter02_01
# 클래스 기반 개발 설명
    # 객체지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트 등
    # 규모가 큰 프로젝트 -> 함수 중심 -> 데이터 방대 -> 복잡
    # 클래스 중심 -> 데이터 중심 -> 구성요소들이 객체로 관리



# 일반적인 코딩
# 차량 1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'white'},
    {'horsepower': 500},
    {'price': 14000}
]

# 차량 2
car_company_2 = 'hyundai'
car_detail_2 = [
    {'color': 'white'},
    {'horsepower': 200},
    {'price': 5000}
]

# 차량 3
car_company_2 = 'kia'
car_detail_2 = [
    {'color': 'silver'},
    {'horsepower': 210},
    {'price': 3000}
]

# 리스트 구조
# 관리가 불편
# 인덱스 접근시 실수 가능성, 삭제불편
car_company_list = ['Ferrari', 'hyundai', 'kia']
car_detail_list = [
    {'color': 'white', 'horsepower': 500, 'price': 14000},
    {'color': 'white', 'horsepower': 200, 'price': 5000},
    {'color': 'silver', 'horsepower': 210, 'price': 3000}
]

del car_company_list[0]
del car_detail_list[0]

print(car_company_list)
print(car_detail_list)

print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키)
cars_dicts = [
    {'car_company' : 'Ferrari', 'car_detail': {'color': 'white', 'horsepower': 500, 'price': 14000}},
    {'car_company' : 'hyundai', 'car_detail': {'color': 'white', 'horsepower': 200, 'price': 5000}},
    {'car_company' : 'kia', 'car_detail': {'color': 'silver', 'horsepower': 210, 'price': 3000}}
]
print(cars_dicts)
del cars_dicts[0]

print(cars_dicts)

print()
print()


# 클래스 구조
# 구조설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 매직 메소드 (스페셜 메소드) - print 문에서 정보 확인용
    # def __str__(self):
    #     return 'str : {} - {}'.format(self._company, self._details)

    # 리프리젠테이션 메소드 - 개발자 입장에서 객체 타입을 인식할 수 있는 공식적인 문자열로 표시할때
    def __repr__(self):
        return 'repr: {} ----- {}'.format(self._company, self._details)

car1 = Car('Ferrari',{'color': 'white', 'horsepower': 500, 'price': 14000})
car2 = Car('hyundai', {'color': 'white', 'horsepower': 200, 'price': 5000})
car3 = Car('kia', {'color': 'silver', 'horsepower': 210, 'price': 3000})


print(car1)
print(car2)
print(car3)

print()
print()


# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print('--------------------')

# 반복(__str__)
for x in car_list:
    # print(repr(x))
    print(x)

print('----------------------------------------------------------')

# 계산기 만들기
# class calc():
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result

#     def power(self):
#         result = self.first ** self.second
#         return result


# a = calc(4545, 575)
# print(a.first)
# print(a.second)
# print('----')
# print(a.add())
# print(a.power())
