# Chapter05-03
# 파이썬 심화
# 클로저 심화
# 외부에 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능

# 클로저(Closure) 사용


def closure_ex1():
    # Free variable (자유변수)
    series = []

    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager



avg_closure = closure_ex1()
print(avg_closure)
print(avg_closure(10))
print(avg_closure(50))
print(avg_closure(100))
print(avg_closure(120))


# function inspection
print(dir(avg_closure))
print()
print(dir(avg_closure.__code__))
# __code__.co_freevars 를 통해 자유변수를 출력할 수 있다.
print(avg_closure.__code__.co_freevars)

print(dir(avg_closure.__closure__[0].cell_contents))

print()
print()


# 잘못된 클로저 사용
# def closure_ex2():
#     # Free variable
#     cnt = 0
#     total = 0

#     def averager(v):
#         cnt += 1
#         total += v
#         return total / cnt
#     return averager

# avg_closure2 = closure_ex2()

# print(avg_closure2(10))


# 수정
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        # List 를 사용해서 append 해주는게 아니라면 nonlocal로 선언을 해주어야 한다.
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()

print(avg_closure2(10))
print(avg_closure2(15))
print(avg_closure2(20))