import random

random_number = random.randint(1, 20)
chance = 4

while chance >= 0:
    # 숫자입력
    guess_number = int(input('기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: '.format(chance)))
    
    # 숫자 추측이 성공한 경우
    if guess_number == random_number:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(4 - (chance - 1)))
        break
    # 숫자 추측 실패했는데 기회가 남아 있을때
    elif guess_number != random_number and chance > 1:
        chance -= 1
        if guess_number < random_number:
            print("Up")
        else:
            print("Down")
    # 숫자 추측 실패했는데 기회 소진 시
    elif guess_number != random_number and chance == 1:
        chance -= 1
        print("아쉽습니다. 정갑은 {}였습니다.".format(random_number))
        break