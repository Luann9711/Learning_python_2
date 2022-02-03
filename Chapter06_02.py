# Chapter06-01
# 병행성(Concurrency)
# 병렬성(Parallelism)
# 이터레이터(Iterator), 제네레이터(Generator)

# 제너레이터는 이터레이터를 반환하는 함수이다 (이터레이터를 생성함)


# Generator  EX 1

def generator_ex1():
    print('Start')
    yield 'A Point'
    
    print('Continue')
    yield 'B Point'

    print('End')

# iter 는 반복 가능한 계체에서  이터레이터를 반환
temp = iter(generator_ex1())

# print(temp)
# print(next(temp))
# print(next(temp))
# print(next(temp))


# for v in generator_ex1():
#     print(v)


# Generator EX 2

temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp2:
    print(i)


for i in temp3:
    print(i)



# Generator EX 3 (중요함수)
# filterfalse, accumulate, chain, product, groupby, takewhile

import itertools

gen1 = itertools.count(1, 2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

# 무한

# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    # print(v)
    pass

print('-------------------------------')

# 필터 반대역할 하는 것
gen3 = itertools.filterfalse(lambda n : n < 3,[1, 2, 3, 4, 5])


for idx in gen3:
    print(idx)

print()


# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])


for v in gen4:
    print(v)


# 연결 1
gen5 = itertools.chain('ABCDE', range(1,11,2))
print(list(gen5))

# 연결 2
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))


# 개별 (개별로 분리해줌)
gen7 = itertools.product('ABCDE')
print(list(gen7))


# 연산 (경우의 수 생성)
gen8 = itertools.product('ABCDEFG', repeat=2)
print(list(gen8))


# 그룹화
gen9 = itertools.groupby('AAAABBBBCCCCCDDDEEEEE')
# print(list(gen9))
for a, b in gen9:
    print(a, ' : ', list(b))