import random

words_dict ={
    '사자': 'lion',
    '호랑이': 'tiger',
    '사과': 'apple',
    '비행기': 'airplane'
}

words = []

for word in words_dict:
    words.append(word)

random.shuffle(words)
print(words)

chance = 3

for i in range(0, len(words)):
    q = words[i]

    for j in range(0, chance):
        user_input = str(input(f'{q} 의 영어 단어를 입력하세요> '))
        english = words_dict[q]

        if user_input.strip().lower() == english.lower():
            print('정답 입니다.')
            break
        else:
            print('틀렸습니다.')
    if user_input != english:
        print(f'정답은 {english}입니다.')

print('모든 문제를 다 제출했습니다.')