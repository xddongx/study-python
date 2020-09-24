import random
import os

def input_check(msg, casting=int):
    while True:
        try:
            user_input = casting(input('몇 일까요? '))
            return user_input
        except:
            continue

chance = 10
count = 0
number = random.randint(1, 99)
os.system('cls')
print('1 부터 99 까지의 숫자를 10번 안에 맞춰 보세요.')

while count < chance:
    count += 1
    user_input = input_check('몇 일까요? ')

    if number == user_input:
        break
    elif user_input < number:
        print(f'{user_input} 보다 큰 숫자 입니다.')
    elif user_input > number:
        print(f'{user_input} 보다 작은 숫자 입니다.')
    else:
        print('아닙니다.')

if user_input == number:
    print(f'성공! {number}이 맞습니다.')
else:
    print(f'실패, 정답은 {number} 입니다.')