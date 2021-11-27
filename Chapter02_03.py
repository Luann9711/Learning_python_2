# Chapter02-03
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

class Car():
    """
    Car Class
    Author : Kim
    Date : 2021.11.17
    Description : Class, Static, Instance Method
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.0

    # 인스턴스 메소드 (self) :  첫번쨰 매개변수로 넘어오게 된 약속
    # 클래스를 기반으로 생성된 인스턴스 자기 내부의 고유의 값을 저장하기 위한 예약어
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 매직 메소드 (스페셜 메소드) - print 문에서 정보 확인용
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    # 리프리젠테이션 메소드 - 개발자 입장에서 객체 타입을 인식할 수 있는 공식적인 문자열로 표시할때
    def __repr__(self):
        return 'repr: {} ----- {}'.format(self._company, self._details)

    # Instance Method
    # self : 객체의 고유한 속성값을 사용
    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info : {} - {}'.format(self._company, self._details.get('horsepower')))
        
    def get_price(self):
        return 'Before Car price -> Company : {}, Price : {}'.format(self._company, self._details.get('price'))

    def get_price_calc(self):
        return 'After Car price -> Company : {}, Price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)


    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please enter the number higher then 1')
            return
        cls.price_per_raise = per
        print('Succeed! Price Inscreased.')
        
    # Static Method   // cls 값이나 self 값을 받을 필요가 없을때 보다 유연하게 사용할때 필요 (가끔)
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'This car is not BMW'

# 자동차 정보
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})


# 전체정보
print(car1.detail_info())
print(car2.detail_info())
print('---------')

# 가격정보 (인상전)
print(car1.get_price())
print(car2.get_price())

# 인상률
Car.price_per_raise = 1.13

# 가격정보 (인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())

# 가격인상 (클래스 메소드 사용)
Car.raise_price(1.5)

# 가격정보 (인상 후 / 클래스 메소드 사용)
print(car1.get_price_calc())
print(car2.get_price_calc())

# --------------------------------------------------------
# static method  사용

# BMW 여부 //인스턴스로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print('-----')

# BMW 여부  //클래스로 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))