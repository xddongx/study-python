'''
1. 1 ~ 99 까지의 숫자 중 램덤 숫자 하나
2. 기회는 10번
3. 사용자 입력 비교
4. up, down 설명
5. 설공, 실패(정답 공개)
6. 포기 생성
'''

import random
import os

os.system('cls')

def input_check(mse, casting=int):
    while True:
        try:
            user_input = casting(input(mse))
            return user_input
        except:
            print('숫자를 입력하세요.')
            continue

answer = random.randint(1, 99)
count = 0
chance = 10

print('*' * 60)
print('1 ~ 99 까지의 숫자 맞추기 게임입니다.    @@포기: -99...@@')
print('*' * 60)

while count <= chance:
    count += 1
    user_input = input_check('숫자를 입력하세요> ')

    if user_input == -99:
        print('포기라니......')
        break

    if user_input == answer:
        break
    elif user_input > answer:
        print('Down!')
    elif user_input < answer:
        print('Up!')

if user_input != answer:
    print(f'정답은 {answer}입니다.')
else:
    print('정답입니다.')
