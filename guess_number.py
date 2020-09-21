'''
Write a programme where the computer randomly generates a number between 0 and 20. The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. This will get you started with the random library if you haven't already used it.
'''

from random import *
first_num, second_num = map(int, input('숫자 범위를 입력해주세요 : ').split())
num = randint(first_num, second_num)

print('총 10번의 기회가 주어집니다.\n')

for i in range(1, 11):
    print(f'{i}번째 기회입니다.')
    user_input = int(input(f'{first_num}와 {second_num} 사이의 숫자를 입력해주세요 : '))
    if user_input == num:
        print('정답을 맞추었습니다.')
        break
    elif user_input > num:
        print(f'{user_input}은 정답보다 높네요.')
    else:
        print(f'{user_input}은 정답보다 낮네요')