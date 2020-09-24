'''
1. 영어단어장 만들기
2. 문제낼 랜덤한 단어장(단어장의 한글) 배열 만들기
3. 단어 맞출 기회
4. 기회만클 정답과 비교
5. 맞추면 정답, 틀리면 정답 출력
'''

import random, os, re

os.system('cls')

word_dict = {
    '사자': 'lion',
    '호랑이': 'tiger',
    '사과': 'apple',
    '바나나': 'banana',
    '음식': 'food'
}

quiz_word = []
for i in word_dict:
    quiz_word.append(i)

random.shuffle(quiz_word)

answer_count = 0
chance = 3

for word in quiz_word:
    count = 0
    while count < chance:
        count += 1
        user_input = input(f'{word}의 영어단어를 입력하세요> ')
        if user_input.lower() == word_dict[word].lower():
            answer_count += 1
            print('정답입니다.')
            break
        else:
            print('틀렸습니다')
            if count == 3:
                print(f'정답은 {word_dict[word].lower()} 입니다.')

print(f'{answer_count}개 맞췄습니다.')