from random import *

# 단어 저장소
dictionaries = ['apple', 'pear', 'cheery']

# 사용자가 입력한 단어 저장
save_letters = []

# 무작위 선택 (sting 으로 저장)
answer = choice(dictionaries)

# 선택된 단어의 길이
lengh_answer = len(answer)

# 사용자에게 글자 수 보여주는 변수
blanks = ['_' for i in range(lengh_answer)]

# 사용자에게 글자 수 보여주기
for blank in blanks:
    print(blank, end='')
print(f'\n총 {len(answer)}글자입니다\n')


for count in range(5, 0, -1):
    # 사용자 글자 입력
    print(f'기회는 {count}번 남았습니다.\n')
    user_input = input('글자 또는 답을 입력하세요 : ')

    # 답을 맞추었을 경우
    if user_input == answer:
        print('정답입니다')
        break
    # 글자를 맞추었을 경우
    elif user_input in answer:
        # 글자를 이미 입력한 경우
        if user_input in save_letters:
            print('이미 입력한 단어입니다')
        # 새로운 글자가 입력 되었을 경우
        else:
            print(f'{user_input}는 단어에 포함이 되어 있습니다.')
            save_letters.append(user_input)
            # 입력된 글자와 답을 비교해가면서 빈칸을 단어로 바꾸기
            for n in range(lengh_answer):
                if answer[n] == user_input:
                    blanks[n] = user_input
    else:
        print('없는 단어입니다.')
    if count == 1:
        print(f'아쉽네요,, 답은 {answer}입니다.')
        break
    print(''.join(blanks))

print('\n수고하셨습니다.')