from random import *

class Hangman:
    # 단어 사전을 초기화 할 때 지정
    def __init__(self, dicts):
        self.dicts = dicts
        self.answer = self.random_choice_answer(self.dicts)
        self.save_letters = []

    def start_menu(self):
        print('행맨 게임에 오신 여러분을 환영합니다.')
        print('단어는 무작위로 출제가 됩니다.')
        print('총 기회는 10번입니다.')

    # 무작위 선택 (sting 으로 저장)
    def random_choice_answer(self, dicts):
        return choice(dicts)

# 단어 저장소
dictionaries = ['apple', 'pear', 'cheery']

player = Hangman(dictionaries)

player.start_menu()

# 사용자가 입력한 단어 저장
save_letters = []


answer = choice(dictionaries)

# 선택된 단어의 길이
lengh_answer = len(answer)

# 사용자에게 글자 수 보여주는 변수
blanks = ['_' for i in range(lengh_answer)]

# 사용자에게 글자 수 보여주기
for blank in blanks:
    print(blank, end='')
print(f'\n총 {len(answer)}글자입니다\n')


for count in range(10, 0, -1):
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