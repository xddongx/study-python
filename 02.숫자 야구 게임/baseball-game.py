'''
1. 컴퓨터가 정한 세 자리의 숫자, 0 ~ 9(중복되지 않은)
2. 같은 자리 같은 숫자 스트라이크
3. 다른 자리 같은 숫자 볼
4. 기회 10번
5. 3스트라이크 종료, 실패 시 정답 공개
6. 포기 생성
'''

import random
import os

os.system('cls')

def input_check(mse, casting=int):
    while True:
        try:
            user_input = []
            for i in range(1, 4):
                while True:
                    num = casting(input(f'{i}{mse}'))
                    if num not in user_input:
                        user_input.append(num)
                        break
            if len(user_input) == 3:
                return user_input
        except:
            print('숫자를 입력하세요.')
            continue

numbers = []
for i in range(3):
    number = random.randint(0, 9)
    while True:
        if number not in numbers:
            numbers.append(number)
            break

print('*' * 60)
print('야구게임 0 ~ 9 까지의 각각 다른 숫자입력> ')
print('1 번째 숫자> 3\n2 번째 숫자> 5\n3 번째 숫자> 7')
print('*' * 60)


count = 0
chance = 10

while count <= chance:
    count += 1
    ball_count = 0
    strike_count = 0

    user_input = input_check('번째 숫자> ')

    for i in range(len(numbers)):
        for j in range(len(user_input)):
            if numbers[i] == user_input[j] and i == j:
                strike_count += 1
            if numbers[i] == user_input[j] and i != j:
                ball_count += 1

    if strike_count >= 3:
        break
    elif strike_count == 0 and ball_count == 0:
        print('아웃!!!!')
    elif strike_count >= 0:
        print(f'{strike_count} strike, {ball_count} ball')



if strike_count == 3:
    print('정답입니다.')
else:
    print('정답은 ', end='')
    for i in numbers:
        print(f'{i} ', end='')
    print('입니다.')