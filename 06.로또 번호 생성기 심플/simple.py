import random, os

count = int(input('로또 번호를 몇개 생성할까요? > '))
for j in range(count):
    lotto = []
    rand_num = random.randint(1, 46)

    for i in range(6):
        while rand_num in lotto:
            rand_num = random.randint(1, 46)
        lotto.append(rand_num)
    lotto.sort()

    print(f'{j + 1}. 로또번호 : {lotto}')












# start = time.time()
#
# number = []
# for i in range(6):
#     number.append(random.randint(1, 43))
#     if i in number:
#         del number[-1]
# number.sort()
# end = time.time()
# total = end - start
# print(number, total)
