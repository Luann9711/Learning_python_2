# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

class Car():
    '''
    Car class
    Author : Luann Kim
    Date:2021.11.16 
    '''

    # 클래스 변수 // 모든 인스턴스가 공유한다
    car_count = 0

    # 인스턴스 메소드 (self) :  첫번쨰 매개변수로 넘어오게 된 약속
    # 클래스를 기반으로 생성된 인스턴스 자기 내부의 고유의 값을 저장하기 위한 예약어
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    # 매직 메소드 (스페셜 메소드) - print 문에서 정보 확인용
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    # 리프리젠테이션 메소드 - 개발자 입장에서 객체 타입을 인식할 수 있는 공식적인 문자열로 표시할때
    def __repr__(self):
        return 'repr: {} ----- {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info : {} - {}'.format(self._company, self._details.get('horsepower')))


car1 = Car('Ferrari',{'color': 'white', 'horsepower': 500, 'price': 14000})
car2 = Car('hyundai', {'color': 'white', 'horsepower': 200, 'price': 5000})
car3 = Car('kia', {'color': 'silver', 'horsepower': 210, 'price': 3000})


# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1 is car2)
print(car1._details == car2._details)

# dir & __dict__ 확인
print(dir(car1))
print(car1.__dict__)

# Doctring
# print(car1.__doc__)
print()

# 디테일
car1.detail_info()
car2.detail_info()
car3.detail_info()

# 클래스가 모두 Car에 속에 있으므로 메모리 주소값이 같다
print(id(car1.__class__),id(car2.__class__))

# 클래스 변수 확인
print(car1.car_count)

# 접근
print(Car.car_count)
print(car1.car_count)
print(car2.car_count)