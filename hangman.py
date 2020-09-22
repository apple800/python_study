from random import *


class Hangman:
    def __init__(self, dicts):
        self.dicts = dicts
        # 정답 저장
        self.answer = self.random_choice_answer(self.dicts)
        # 사용자가 입력한 단어 저장
        self.save_letters = []
        # 선택된 단어의 길이
        self.lengh_answer = len(self.answer)
        # 사용자에게 글자 수 보여주는 변수
        self.blanks = ['_' for i in range(self.lengh_answer)]

    def start_menu(self):
        print('행맨 게임에 오신 여러분을 환영합니다.')
        print('단어는 무작위로 출제가 됩니다.')
        print('총 기회는 10번입니다.')

    # 무작위 선택 (string 으로 저장)
    def random_choice_answer(self, dicts):
        return choice(dicts)

    def play(self):
        # 사용자에게 글자 수 보여주기
        for blank in self.blanks:
            print(blank, end='')
        print(f'\n총 {len(self.answer)}글자입니다\n')

        for count in range(10, 0, -1):
            # 사용자 글자 입력
            print(f'기회는 {count}번 남았습니다.\n')
            user_input = input('글자 또는 답을 입력하세요 : ')

            # 답을 맞추었을 경우
            if user_input == self.answer:
                print('정답입니다')
                break
            # 글자를 맞추었을 경우
            elif user_input in self.answer:
                # 글자를 이미 입력한 경우
                if user_input in self.save_letters:
                    print('이미 입력한 단어입니다')
                # 새로운 글자가 입력 되었을 경우
                else:
                    print(f'{user_input}는 단어에 포함이 되어 있습니다.')
                    self.save_letters.append(user_input)
                    # 입력된 글자와 답을 비교해가면서 빈칸을 단어로 바꾸기
                    for n in range(self.lengh_answer):
                        if self.answer[n] == user_input:
                            self.blanks[n] = user_input
                            continue
                    if '_' not in self.blanks:
                        print('정답입니다.')
                        break
            else:
                print('없는 단어입니다.')

            if count == 1:
                print(f'아쉽네요,, 답은 {answer}입니다.')
                break
            print(''.join(self.blanks))

        print('\n수고하셨습니다.')


# 단어 저장소
dictionaries = ['apple', 'pear', 'cheery']

player = Hangman(dictionaries)

player.start_menu()
player.play()
