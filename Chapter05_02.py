# Chapter05-02
# 파이썬 심화
# 클로저 기초

# 파이썬 변수 범위(scope)

# 예제 1
def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(10)

# 예제 2
b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(30)

print('---------------------------')

# 예제 3

c = 30

def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40

print('>>',c)
func_v3(10)
print('>>>',c)